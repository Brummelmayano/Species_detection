import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models.user import User

# Configuration de la base de données de test
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def test_user():
    db = TestingSessionLocal()
    hashed_password = "hashed_password"
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password=hashed_password,
        full_name="Test User"
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

class TestAuthAPI:
    def test_register_success(self, client):
        user_data = {
            "email": "new@example.com",
            "username": "newuser",
            "password": "password123",
            "full_name": "New User"
        }
        response = client.post("/auth/register", json=user_data)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_register_duplicate_email(self, client, test_user):
        user_data = {
            "email": "test@example.com",  # Same email as test_user
            "username": "differentuser",
            "password": "password123"
        }
        response = client.post("/auth/register", json=user_data)
        assert response.status_code == 400
        assert "Email déjà enregistré" in response.json()["detail"]

    def test_login_success(self, client, test_user):
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        response = client.post("/auth/login", data=login_data)
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_login_wrong_credentials(self, client):
        login_data = {
            "username": "wronguser",
            "password": "wrongpass"
        }
        response = client.post("/auth/login", data=login_data)
        assert response.status_code == 401
        assert "Nom d'utilisateur ou mot de passe incorrect" in response.json()["detail"]

    def test_get_current_user(self, client, test_user):
        # First login to get token
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        login_response = client.post("/auth/login", data=login_data)
        token = login_response.json()["access_token"]

        # Use token to access protected route
        headers = {"Authorization": f"Bearer {token}"}
        response = client.get("/auth/me", headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"

    def test_get_current_user_invalid_token(self, client):
        headers = {"Authorization": "Bearer invalid_token"}
        response = client.get("/auth/me", headers=headers)
        assert response.status_code == 401

class TestImagesAPI:
    def test_get_images_unauthorized(self, client):
        response = client.get("/images/")
        assert response.status_code == 401

    def test_get_images_authorized(self, client, test_user):
        # Login first
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        login_response = client.post("/auth/login", data=login_data)
        token = login_response.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        response = client.get("/images/", headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_upload_image_unauthorized(self, client):
        response = client.post("/images/upload?project_id=1")
        assert response.status_code == 401

    # Note: Upload test would require mocking file upload and MinIO
    # For now, we test the authorization part

class TestProjectsAPI:
    def test_get_projects_unauthorized(self, client):
        response = client.get("/projects/")
        assert response.status_code == 401

    def test_get_projects_authorized(self, client, test_user):
        # Login first
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        login_response = client.post("/auth/login", data=login_data)
        token = login_response.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        response = client.get("/projects/", headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)
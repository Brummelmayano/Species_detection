import pytest
from unittest.mock import Mock, patch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.services.auth_service import AuthService
from app.services.speciesnet_service import SpeciesNetService
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin

# Configuration de la base de données de test
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

class TestAuthService:
    def test_authenticate_user_success(self, db_session):
        # Créer un utilisateur de test
        hashed_password = "hashed_password"
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password=hashed_password
        )
        db_session.add(user)
        db_session.commit()

        auth_service = AuthService(db_session)

        with patch('app.utils.jwt.verify_password', return_value=True):
            result = auth_service.authenticate_user("testuser", "password")
            assert result == user

    def test_authenticate_user_wrong_username(self, db_session):
        auth_service = AuthService(db_session)
        result = auth_service.authenticate_user("nonexistent", "password")
        assert result == False

    def test_authenticate_user_wrong_password(self, db_session):
        # Créer un utilisateur de test
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashed_password"
        )
        db_session.add(user)
        db_session.commit()

        auth_service = AuthService(db_session)

        with patch('app.utils.jwt.verify_password', return_value=False):
            result = auth_service.authenticate_user("testuser", "wrongpassword")
            assert result == False

    def test_create_user_success(self, db_session):
        auth_service = AuthService(db_session)
        user_data = UserCreate(
            email="new@example.com",
            username="newuser",
            password="password123",
            full_name="New User"
        )

        with patch('app.utils.jwt.get_password_hash', return_value="hashed_password"):
            result = auth_service.create_user(user_data)
            assert result.email == "new@example.com"
            assert result.username == "newuser"
            assert result.hashed_password == "hashed_password"

    def test_create_user_email_exists(self, db_session):
        # Créer un utilisateur existant
        user = User(
            email="existing@example.com",
            username="existing",
            hashed_password="hashed"
        )
        db_session.add(user)
        db_session.commit()

        auth_service = AuthService(db_session)
        user_data = UserCreate(
            email="existing@example.com",
            username="newuser",
            password="password123"
        )

        with pytest.raises(Exception) as exc_info:
            auth_service.create_user(user_data)
        assert "Email déjà enregistré" in str(exc_info.value)

    def test_login_success(self, db_session):
        # Créer un utilisateur de test
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashed_password"
        )
        db_session.add(user)
        db_session.commit()

        auth_service = AuthService(db_session)
        login_data = UserLogin(username="testuser", password="password")

        with patch('app.utils.jwt.verify_password', return_value=True), \
             patch('app.utils.jwt.create_access_token', return_value="token123"):
            result = auth_service.login(login_data)
            assert result["access_token"] == "token123"
            assert result["token_type"] == "bearer"

    def test_login_failure(self, db_session):
        auth_service = AuthService(db_session)
        login_data = UserLogin(username="wronguser", password="password")

        with pytest.raises(Exception) as exc_info:
            auth_service.login(login_data)
        assert "Nom d'utilisateur ou mot de passe incorrect" in str(exc_info.value)

class TestSpeciesNetService:
    @pytest.mark.asyncio
    async def test_detect_species_success(self):
        service = SpeciesNetService()

        mock_response_data = {
            "detections": [
                {
                    "species": "Panthera leo",
                    "confidence": 0.95,
                    "bbox": {
                        "x_min": 10,
                        "y_min": 20,
                        "x_max": 100,
                        "y_max": 120,
                        "width": 90,
                        "height": 100
                    }
                }
            ]
        }

        with patch('httpx.AsyncClient') as mock_client:
            mock_response = Mock()
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None

            mock_client.return_value.__aenter__.return_value.post.return_value = mock_response

            result = await service.detect_species("http://example.com/image.jpg")

            assert len(result) == 1
            assert result[0]["species_name"] == "Panthera leo"
            assert result[0]["confidence_score"] == 0.95
            assert result[0]["bbox_x_min"] == 10

    @pytest.mark.asyncio
    async def test_detect_species_request_error(self):
        service = SpeciesNetService()

        with patch('httpx.AsyncClient') as mock_client:
            mock_client.return_value.__aenter__.return_value.post.side_effect = Exception("Network error")

            with pytest.raises(Exception) as exc_info:
                await service.detect_species("http://example.com/image.jpg")
            assert "Erreur de communication avec SpeciesNet" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_detect_species_http_error(self):
        service = SpeciesNetService()

        with patch('httpx.AsyncClient') as mock_client:
            mock_response = Mock()
            mock_response.raise_for_status.side_effect = Exception("HTTP 500")
            mock_response.status_code = 500

            mock_client.return_value.__aenter__.return_value.post.return_value = mock_response

            with pytest.raises(Exception) as exc_info:
                await service.detect_species("http://example.com/image.jpg")
            assert "Erreur du service SpeciesNet" in str(exc_info.value)
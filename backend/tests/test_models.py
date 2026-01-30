import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.user import User
from app.models.project import Project
from app.models.image import Image
from app.models.detection import Detection

# Configuration de la base de données de test en mémoire
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

class TestUserModel:
    def test_user_creation(self, db_session):
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashedpass",
            full_name="Test User"
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        assert user.id is not None
        assert user.email == "test@example.com"
        assert user.username == "testuser"
        assert user.hashed_password == "hashedpass"
        assert user.full_name == "Test User"
        assert user.is_active == True
        assert user.is_admin == False

    def test_user_unique_constraints(self, db_session):
        # Créer le premier utilisateur
        user1 = User(
            email="test@example.com",
            username="testuser",
            hashed_password="hashedpass"
        )
        db_session.add(user1)
        db_session.commit()

        # Tenter de créer un utilisateur avec le même email
        user2 = User(
            email="test@example.com",
            username="testuser2",
            hashed_password="hashedpass2"
        )
        db_session.add(user2)
        with pytest.raises(Exception):  # IntegrityError
            db_session.commit()

class TestProjectModel:
    def test_project_creation(self, db_session):
        # Créer un utilisateur d'abord
        user = User(
            email="owner@example.com",
            username="owner",
            hashed_password="hashedpass"
        )
        db_session.add(user)
        db_session.commit()

        project = Project(
            name="Test Project",
            description="A test project",
            owner_id=user.id
        )
        db_session.add(project)
        db_session.commit()
        db_session.refresh(project)

        assert project.id is not None
        assert project.name == "Test Project"
        assert project.description == "A test project"
        assert project.owner_id == user.id

class TestImageModel:
    def test_image_creation(self, db_session):
        # Créer un utilisateur et un projet
        user = User(
            email="uploader@example.com",
            username="uploader",
            hashed_password="hashedpass"
        )
        db_session.add(user)
        db_session.commit()

        project = Project(
            name="Test Project",
            description="A test project",
            owner_id=user.id
        )
        db_session.add(project)
        db_session.commit()

        image = Image(
            filename="test.jpg",
            original_filename="original.jpg",
            file_path="/path/to/file.jpg",
            file_size=1024,
            mime_type="image/jpeg",
            width=800,
            height=600,
            project_id=project.id,
            uploaded_by_id=user.id
        )
        db_session.add(image)
        db_session.commit()
        db_session.refresh(image)

        assert image.id is not None
        assert image.filename == "test.jpg"
        assert image.processing_status == "pending"

class TestDetectionModel:
    def test_detection_creation(self, db_session):
        # Créer les entités nécessaires
        user = User(
            email="uploader@example.com",
            username="uploader",
            hashed_password="hashedpass"
        )
        db_session.add(user)
        db_session.commit()

        project = Project(
            name="Test Project",
            description="A test project",
            owner_id=user.id
        )
        db_session.add(project)
        db_session.commit()

        image = Image(
            filename="test.jpg",
            original_filename="original.jpg",
            file_path="/path/to/file.jpg",
            project_id=project.id,
            uploaded_by_id=user.id
        )
        db_session.add(image)
        db_session.commit()

        detection = Detection(
            image_id=image.id,
            species_name="Panthera leo",
            confidence_score=0.95,
            bbox_x_min=10,
            bbox_y_min=20,
            bbox_x_max=100,
            bbox_y_max=120
        )
        db_session.add(detection)
        db_session.commit()
        db_session.refresh(detection)

        assert detection.id is not None
        assert detection.species_name == "Panthera leo"
        assert detection.confidence_score == 0.95
        assert detection.bbox_x_min == 10
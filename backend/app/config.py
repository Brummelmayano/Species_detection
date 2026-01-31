from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Base de données
    # Par défaut, utilise PostgreSQL pour éviter l'usage accidentel de SQLite en production.
    # Pour le développement local, définir DATABASE_URL dans .env vers SQLite si besoin.
    # Exemple production : postgresql://user:password@localhost/species_detection
    # Exemple développement : sqlite:///./species_detection.db
    database_url: str = "postgresql://user:password@localhost/species_detection"

    # JWT
    secret_key: str = "your-secret-key-here"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # MinIO
    minio_endpoint: str = "localhost:9000"
    minio_access_key: str = "minioadmin"
    minio_secret_key: str = "minioadmin"
    minio_secure: bool = False
    minio_bucket_name: str = "species-images"

    # SpeciesNet Service
    speciesnet_url: str = "http://localhost:8001"

    # Redis (pour Celery)
    redis_url: str = "redis://localhost:6379/0"


    class Config:
        env_file = ".env"

# IMPORTANT :
# En production, il est impératif de définir la variable d'environnement DATABASE_URL
# vers une base PostgreSQL pour éviter l'utilisation accidentelle de SQLite.
# Voir la documentation dans README.md pour plus de détails.

settings = Settings()
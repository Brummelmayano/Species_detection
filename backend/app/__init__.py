from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .routers import auth, projects, images
from .database import engine, Base
from . import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Créer les tables de la base de données au démarrage
    Base.metadata.create_all(bind=engine)
    yield
    # Nettoyage si nécessaire

app = FastAPI(
    title="Species Detection API",
    description="API pour la détection automatique d'espèces dans les images",
    version="1.0.0",
    lifespan=lifespan
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À configurer selon les besoins en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware de sécurité pour les hôtes de confiance
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1", "0.0.0.0"]  # À configurer selon l'environnement
)

# Inclure les routers
app.include_router(auth, prefix="/auth", tags=["authentification"])
app.include_router(projects, prefix="/projects", tags=["projets"])
app.include_router(images, prefix="/images", tags=["images"])

@app.get("/")
async def root():
    return {"message": "API de détection d'espèces"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
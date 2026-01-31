from contextlib import asynccontextmanager
import tempfile
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routers
app.include_router(auth, prefix="/auth", tags=["authentification"])
app.include_router(projects, prefix="/projects", tags=["projets"])
app.include_router(images, prefix="/images", tags=["images"])

# Monter le répertoire temporaire pour servir les fichiers uploadés
app.mount("/temp", StaticFiles(directory=tempfile.gettempdir()), name="temp")

@app.get("/")
async def root():
    return {"message": "API de détection d'espèces"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
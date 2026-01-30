import os
import uuid
import tempfile
import mimetypes
from typing import List
from PIL import Image as PILImage
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Form
from sqlalchemy.orm import Session
from .. import database, models
from ..schemas import Image, ImageWithUrl, ImageCreate
from ..routers.auth import get_current_user
from ..services.speciesnet_service import SpeciesNetService

router = APIRouter()

# Configuration pour le stockage temporaire
TEMP_DIR = tempfile.gettempdir()
ALLOWED_MIME_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"]
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
MAX_WIDTH = 4096
MAX_HEIGHT = 4096

def validate_image_file(file: UploadFile) -> dict:
    """Valide le fichier image et retourne les métadonnées"""
    # Vérifier la taille du fichier
    file_size = len(file.file.read())
    file.file.seek(0)  # Remettre le curseur au début

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Fichier trop volumineux (max 10MB)")

    # Vérifier le type MIME
    mime_type, _ = mimetypes.guess_type(file.filename)
    if mime_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(status_code=400, detail=f"Type de fichier non supporté: {mime_type}")

    # Ouvrir l'image avec PIL pour vérifier les dimensions
    try:
        image = PILImage.open(file.file)
        width, height = image.size

        if width > MAX_WIDTH or height > MAX_HEIGHT:
            raise HTTPException(status_code=400, detail=f"Dimensions trop grandes (max {MAX_WIDTH}x{MAX_HEIGHT})")

        # Remettre le curseur au début après PIL
        file.file.seek(0)

        return {
            "file_size": file_size,
            "mime_type": mime_type,
            "width": width,
            "height": height
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Fichier image invalide: {str(e)}")

def save_temp_file(file: UploadFile) -> str:
    """Sauvegarde temporairement le fichier et retourne le chemin"""
    # Générer un nom de fichier unique
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    temp_path = os.path.join(TEMP_DIR, unique_filename)

    # Sauvegarder le fichier
    with open(temp_path, "wb") as buffer:
        content = file.file.read()
        buffer.write(content)

    return temp_path

@router.post("/upload", response_model=Image)
async def upload_image(
    project_id: int = Form(...),
    file: UploadFile = File(...),
    latitude: float = Form(None),
    longitude: float = Form(None),
    captured_at: str = Form(None),
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Upload d'une seule image avec validation et stockage temporaire"""

    # Valider le fichier
    metadata = validate_image_file(file)

    # Sauvegarder temporairement
    temp_path = save_temp_file(file)

    # Créer l'entrée en base de données
    db_image = models.Image(
        filename=os.path.basename(temp_path),
        original_filename=file.filename,
        file_path=temp_path,  # Pour l'instant, chemin temporaire
        file_size=metadata["file_size"],
        mime_type=metadata["mime_type"],
        width=metadata["width"],
        height=metadata["height"],
        latitude=latitude,
        longitude=longitude,
        captured_at=captured_at,
        project_id=project_id,
        uploaded_by_id=current_user.id,
        processing_status="pending"
    )

    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    # Préparer pour SpeciesNet (asynchrone)
    # TODO: Déclencher le traitement SpeciesNet en arrière-plan

    return db_image

@router.post("/bulk-upload", response_model=List[Image])
async def bulk_upload_images(
    project_id: int = Form(...),
    files: List[UploadFile] = File(...),
    latitude: float = Form(None),
    longitude: float = Form(None),
    captured_at: str = Form(None),
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Upload en masse d'images avec validation et stockage temporaire"""

    if len(files) > 20:  # Limiter à 20 fichiers par upload
        raise HTTPException(status_code=400, detail="Maximum 20 fichiers par upload en masse")

    uploaded_images = []

    for file in files:
        try:
            # Valider le fichier
            metadata = validate_image_file(file)

            # Sauvegarder temporairement
            temp_path = save_temp_file(file)

            # Créer l'entrée en base de données
            db_image = models.Image(
                filename=os.path.basename(temp_path),
                original_filename=file.filename,
                file_path=temp_path,
                file_size=metadata["file_size"],
                mime_type=metadata["mime_type"],
                width=metadata["width"],
                height=metadata["height"],
                latitude=latitude,
                longitude=longitude,
                captured_at=captured_at,
                project_id=project_id,
                uploaded_by_id=current_user.id,
                processing_status="pending"
            )

            db.add(db_image)
            uploaded_images.append(db_image)

        except Exception as e:
            # En cas d'erreur sur un fichier, continuer avec les autres
            # TODO: Logger l'erreur
            continue

    db.commit()

    # Rafraîchir tous les objets
    for img in uploaded_images:
        db.refresh(img)

    # TODO: Déclencher le traitement SpeciesNet en arrière-plan pour toutes les images

    return uploaded_images

@router.get("/", response_model=List[ImageWithUrl])
async def get_images(
    project_id: int = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Récupère la liste des images avec pagination"""

    query = db.query(models.Image)

    if project_id:
        query = query.filter(models.Image.project_id == project_id)

    # TODO: Vérifier les permissions d'accès au projet

    images = query.offset(skip).limit(limit).all()

    # Ajouter les URLs (pour l'instant, URLs temporaires)
    result = []
    for img in images:
        img_dict = img.__dict__.copy()
        img_dict["url"] = f"/temp/{img.filename}"  # TODO: URL MinIO
        result.append(ImageWithUrl(**img_dict))

    return result

@router.get("/{image_id}", response_model=ImageWithUrl)
async def get_image(
    image_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Récupère une image spécifique"""

    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image non trouvée")

    # TODO: Vérifier les permissions d'accès

    img_dict = image.__dict__.copy()
    img_dict["url"] = f"/temp/{image.filename}"  # TODO: URL MinIO

    return ImageWithUrl(**img_dict)

@router.delete("/{image_id}")
async def delete_image(
    image_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Supprime une image"""

    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image non trouvée")

    # TODO: Vérifier les permissions (seul le propriétaire ou admin)

    # Supprimer le fichier temporaire
    if os.path.exists(image.file_path):
        os.remove(image.file_path)

    # Supprimer de la base de données
    db.delete(image)
    db.commit()

    return {"message": "Image supprimée avec succès"}
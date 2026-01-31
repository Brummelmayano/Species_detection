import os
import uuid
import tempfile
import mimetypes
import random
from typing import List
from datetime import datetime
from PIL import Image as PILImage
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Form
from sqlalchemy.orm import Session
from .. import database, models
from ..schemas import Image, ImageWithUrl, ImageCreate, Detection, ImageWithUrlAndCount
from ..routers.auth import get_current_user
from ..services.speciesnet_service import SpeciesNetService
from ..repositories.detection_repository import DetectionRepository

def parse_captured_at(captured_at_str: str) -> datetime:
    """Parse captured_at string to datetime, return 400 on invalid format"""
    if not captured_at_str:
        return None
    try:
        return datetime.fromisoformat(captured_at_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Format de captured_at invalide. Utilisez le format ISO 8601.")

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

def generate_mock_detections(image_id: int, image_width: int, image_height: int) -> List[dict]:
    """Génère 1-3 détections mock pour une image"""
    species_list = ["Lion", "Elephant", "Giraffe", "Zebra", "Leopard", "Buffalo", "Rhino", "Cheetah", "Hyena", "Wildebeest"]
    num_detections = random.randint(1, 3)
    detections = []
    
    for _ in range(num_detections):
        bbox_x_min = random.uniform(0, image_width * 0.7)
        bbox_y_min = random.uniform(0, image_height * 0.7)
        bbox_width = random.uniform(50, image_width * 0.3)
        bbox_height = random.uniform(50, image_height * 0.3)
        bbox_x_max = bbox_x_min + bbox_width
        bbox_y_max = bbox_y_min + bbox_height
        
        detection = {
            "image_id": image_id,
            "species_name": random.choice(species_list),
            "confidence_score": round(random.uniform(0.65, 0.98), 2),
            "bbox_x_min": int(bbox_x_min),
            "bbox_y_min": int(bbox_y_min),
            "bbox_x_max": int(bbox_x_max),
            "bbox_y_max": int(bbox_y_max),
            "bbox_width": int(bbox_width),
            "bbox_height": int(bbox_height),
            "validated": "pending"
        }
        detections.append(detection)
    
    return detections

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

    # Parser captured_at
    parsed_captured_at = parse_captured_at(captured_at)

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
        captured_at=parsed_captured_at,
        project_id=project_id,
        uploaded_by_id=current_user.id,
        processing_status="pending"
    )

    db.add(db_image)
    db.commit()
    db.refresh(db_image)

    # Générer les détections mock
    detection_repo = DetectionRepository(db)
    mock_detections = generate_mock_detections(db_image.id, db_image.width, db_image.height)
    detection_repo.bulk_create_detections(mock_detections)

    # Mettre à jour le statut de l'image
    db_image.processing_status = "completed"
    db_image.processing_completed_at = datetime.now()
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

            # Parser captured_at
            parsed_captured_at = parse_captured_at(captured_at)

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
                captured_at=parsed_captured_at,
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

    # Générer les détections mock pour chaque image
    detection_repo = DetectionRepository(db)
    for img in uploaded_images:
        mock_detections = generate_mock_detections(img.id, img.width, img.height)
        detection_repo.bulk_create_detections(mock_detections)
        img.processing_status = "completed"
        img.processing_completed_at = datetime.now()

    db.commit()

    # Rafraîchir toutes les images
    for img in uploaded_images:
        db.refresh(img)

    # TODO: Déclencher le traitement SpeciesNet en arrière-plan pour toutes les images

    return uploaded_images

@router.get("/", response_model=List[ImageWithUrlAndCount])
async def get_images(
    project_id: int = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Récupère la liste des images avec pagination (filtrées par propriété de projet)"""

    # Vérifier les permissions : ne montrer que les images des projets de l'utilisateur
    query = (
        db.query(models.Image)
        .join(models.Project, models.Image.project_id == models.Project.id)
        .filter(models.Project.owner_id == current_user.id)
    )

    if project_id:
        # Vérifier que le projet appartient à l'utilisateur
        project = db.query(models.Project).filter(
            models.Project.id == project_id,
            models.Project.owner_id == current_user.id
        ).first()
        if not project:
            raise HTTPException(status_code=403, detail="Accès non autorisé à ce projet")
        query = query.filter(models.Image.project_id == project_id)

    images = query.offset(skip).limit(limit).all()

    # Ajouter les URLs et les compteurs de détections
    result = []
    for img in images:
        img_dict = {
            "id": img.id,
            "filename": img.filename,
            "original_filename": img.original_filename,
            "file_path": img.file_path,
            "file_size": img.file_size,
            "mime_type": img.mime_type,
            "width": img.width,
            "height": img.height,
            "latitude": img.latitude,
            "longitude": img.longitude,
            "captured_at": img.captured_at,
            "uploaded_at": img.uploaded_at,
            "project_id": img.project_id,
            "uploaded_by_id": img.uploaded_by_id,
            "processing_status": img.processing_status,
            "processing_started_at": img.processing_started_at,
            "processing_completed_at": img.processing_completed_at,
            "url": f"/temp/{img.filename}",
        }
        # Calculer le nombre de détections
        detection_count = db.query(models.Detection).filter(
            models.Detection.image_id == img.id
        ).count()
        img_dict["detection_count"] = detection_count
        result.append(ImageWithUrlAndCount(**img_dict))

    return result

@router.get("/{image_id}", response_model=ImageWithUrl)
async def get_image(
    image_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Récupère une image spécifique (vérification de propriété)"""

    # Vérifier les permissions : l'image doit appartenir à un projet de l'utilisateur
    image = (
        db.query(models.Image)
        .join(models.Project, models.Image.project_id == models.Project.id)
        .filter(models.Image.id == image_id, models.Project.owner_id == current_user.id)
        .first()
    )
    
    if not image:
        raise HTTPException(status_code=404, detail="Image non trouvée")

    img_dict = {
        "id": image.id,
        "filename": image.filename,
        "original_filename": image.original_filename,
        "file_path": image.file_path,
        "file_size": image.file_size,
        "mime_type": image.mime_type,
        "width": image.width,
        "height": image.height,
        "latitude": image.latitude,
        "longitude": image.longitude,
        "captured_at": image.captured_at,
        "uploaded_at": image.uploaded_at,
        "project_id": image.project_id,
        "uploaded_by_id": image.uploaded_by_id,
        "processing_status": image.processing_status,
        "processing_started_at": image.processing_started_at,
        "processing_completed_at": image.processing_completed_at,
        "project": image.project,
        "uploaded_by": image.uploaded_by,
        "detections": image.detections,
        "url": f"/temp/{image.filename}"
    }

    return ImageWithUrl(**img_dict)

@router.get("/{image_id}/detections", response_model=List[Detection])
async def get_image_detections(
    image_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Récupère toutes les détections d'une image (vérification de propriété)"""

    # Vérifier les permissions : l'image doit appartenir à un projet de l'utilisateur
    image = (
        db.query(models.Image)
        .join(models.Project, models.Image.project_id == models.Project.id)
        .filter(models.Image.id == image_id, models.Project.owner_id == current_user.id)
        .first()
    )
    
    if not image:
        raise HTTPException(status_code=403, detail="Accès non autorisé")

    detection_repo = DetectionRepository(db)
    detections = detection_repo.get_detections_by_image(image_id)

    return detections

@router.delete("/{image_id}")
async def delete_image(
    image_id: int,
    db: Session = Depends(database.get_db),
    current_user = Depends(get_current_user)
):
    """Supprime une image (vérification de propriété)"""

    # Vérifier les permissions : l'image doit appartenir à un projet de l'utilisateur
    image = (
        db.query(models.Image)
        .join(models.Project, models.Image.project_id == models.Project.id)
        .filter(models.Image.id == image_id, models.Project.owner_id == current_user.id)
        .first()
    )
    
    if not image:
        raise HTTPException(status_code=403, detail="Accès non autorisé")

    # Supprimer le fichier temporaire
    if os.path.exists(image.file_path):
        os.remove(image.file_path)

    # Supprimer de la base de données
    db.delete(image)
    db.commit()

    return {"message": "Image supprimée avec succès"}
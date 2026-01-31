from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .project import Project
from .user import User
from .detection import Detection

class ImageBase(BaseModel):
    filename: str
    original_filename: str
    file_path: str
    file_size: Optional[int] = None
    mime_type: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    captured_at: Optional[datetime] = None

class ImageCreate(BaseModel):
    project_id: int
    file: bytes
    filename: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    captured_at: Optional[datetime] = None

class ImageUpdate(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    captured_at: Optional[datetime] = None

class Image(ImageBase):
    id: int
    uploaded_at: datetime
    project_id: int
    uploaded_by_id: int
    processing_status: str
    processing_started_at: Optional[datetime]
    processing_completed_at: Optional[datetime]
    project: Project
    uploaded_by: User
    detections: List[Detection] = []

    class Config:
        from_attributes = True

class ImageWithUrl(Image):
    url: str

    class Config:
        from_attributes = True

class ImageWithUrlAndCount(BaseModel):
    """Schéma pour les listes d'images avec URL et compteur de détections"""
    id: int
    filename: str
    original_filename: str
    file_path: str
    file_size: Optional[int] = None
    mime_type: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    captured_at: Optional[datetime] = None
    uploaded_at: datetime
    project_id: int
    uploaded_by_id: int
    processing_status: str
    processing_started_at: Optional[datetime]
    processing_completed_at: Optional[datetime]
    url: str
    detection_count: int = 0

    class Config:
        from_attributes = True
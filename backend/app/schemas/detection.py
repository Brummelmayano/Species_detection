from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .user import User

class DetectionBase(BaseModel):
    species_name: str
    confidence_score: float
    bbox_x_min: float
    bbox_y_min: float
    bbox_x_max: float
    bbox_y_max: float
    bbox_width: Optional[float] = None
    bbox_height: Optional[float] = None

class DetectionCreate(DetectionBase):
    image_id: int

class DetectionUpdate(BaseModel):
    species_name: Optional[str] = None
    confidence_score: Optional[float] = None
    bbox_x_min: Optional[float] = None
    bbox_y_min: Optional[float] = None
    bbox_x_max: Optional[float] = None
    bbox_y_max: Optional[float] = None
    validated: Optional[str] = None
    notes: Optional[str] = None

class Detection(DetectionBase):
    id: int
    image_id: int
    created_at: datetime
    validated: str
    validated_by_id: Optional[int]
    notes: Optional[str]
    validated_by: Optional[User]

    class Config:
        from_attributes = True
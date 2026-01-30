from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .user import User

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_public: bool = False

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None

class Project(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    owner: User

    class Config:
        from_attributes = True

class ProjectWithStats(Project):
    image_count: int = 0
    detection_count: int = 0

    class Config:
        from_attributes = True
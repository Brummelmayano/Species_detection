
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database
from ..schemas import Project, ProjectCreate, ProjectUpdate, ProjectWithStats
from ..routers.auth import get_current_user
from ..services.project_service import ProjectService

router = APIRouter()


@router.get("/", response_model=List[ProjectWithStats])
async def get_projects(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user = Depends(get_current_user)):
    service = ProjectService(db)
    projects = service.get_projects(current_user, skip, limit)
    project_ids = [p.id for p in projects]
    image_counts, detection_counts = service.project_repo.get_projects_stats_bulk(project_ids) if project_ids else ({}, {})
    result = []
    for p in projects:
        stats = {
            "image_count": image_counts.get(p.id, 0),
            "detection_count": detection_counts.get(p.id, 0)
        }
        # Construction du modèle de réponse ProjectWithStats
        project_dict = {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "is_public": p.is_public,
            "owner_id": p.owner_id,
            "created_at": p.created_at,
            "updated_at": p.updated_at,
            "image_count": stats["image_count"],
            "detection_count": stats["detection_count"]
        }
        result.append(ProjectWithStats(**project_dict))
    return result


@router.post("/", response_model=Project)
async def create_project(project: ProjectCreate, db: Session = Depends(database.get_db), current_user = Depends(get_current_user)):
    service = ProjectService(db)
    return service.create_project(project, current_user)


@router.get("/{project_id}", response_model=ProjectWithStats)
async def get_project(project_id: int, db: Session = Depends(database.get_db), current_user = Depends(get_current_user)):
    service = ProjectService(db)
    return service.get_project_with_stats(project_id, current_user)


@router.put("/{project_id}", response_model=Project)
async def update_project(project_id: int, project_update: ProjectUpdate, db: Session = Depends(database.get_db), current_user = Depends(get_current_user)):
    service = ProjectService(db)
    return service.update_project(project_id, project_update, current_user)


@router.delete("/{project_id}")
async def delete_project(project_id: int, db: Session = Depends(database.get_db), current_user = Depends(get_current_user)):
    service = ProjectService(db)
    service.delete_project(project_id, current_user)
    return {"message": "Projet supprimé avec succès"}
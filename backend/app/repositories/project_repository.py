from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from .. import models
from ..schemas import ProjectUpdate

class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_project(self, project_id: int):
        return self.db.query(models.Project).options(joinedload(models.Project.owner)).filter(models.Project.id == project_id).first()

    def get_projects_by_owner(self, owner_id: int, skip: int = 0, limit: int = 100):
        return (
            self.db.query(models.Project)
            .filter(models.Project.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_all_projects(self, skip: int = 0, limit: int = 100):
        return self.db.query(models.Project).offset(skip).limit(limit).all()

    def create_project(self, project_data: dict):
        db_project = models.Project(**project_data)
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def update_project(self, project_id: int, project_update: ProjectUpdate):
        db_project = self.get_project(project_id)
        if not db_project:
            return None
        update_data = project_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_project, key, value)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def delete_project(self, project_id: int):
        db_project = self.get_project(project_id)
        if not db_project:
            return None
        self.db.delete(db_project)
        self.db.commit()
        return db_project

    def get_project_stats(self, project_id: int):
        project = self.get_project(project_id)
        if not project:
            return None
        image_count = (
            self.db.query(func.count(models.Image.id))
            .filter(models.Image.project_id == project_id)
            .scalar()
        )
        detection_count = (
            self.db.query(func.count(models.Detection.id))
            .join(models.Image, models.Image.id == models.Detection.image_id)
            .filter(models.Image.project_id == project_id)
            .scalar()
        )
        return {"image_count": image_count, "detection_count": detection_count}

    def get_projects_stats_bulk(self, project_ids):
        """Récupère les compteurs d'images et détections pour tous les projets en une seule requête"""
        if not project_ids:
            return {}, {}
        
        # Récupère le nombre d'images par projet
        image_counts = dict(
            self.db.query(models.Image.project_id, func.count(models.Image.id))
            .filter(models.Image.project_id.in_(project_ids))
            .group_by(models.Image.project_id)
            .all()
        )
        # Récupère le nombre de détections par projet
        detection_counts = dict(
            self.db.query(models.Image.project_id, func.count(models.Detection.id))
            .join(models.Detection, models.Image.id == models.Detection.image_id)
            .filter(models.Image.project_id.in_(project_ids))
            .group_by(models.Image.project_id)
            .all()
        )
        return image_counts, detection_counts

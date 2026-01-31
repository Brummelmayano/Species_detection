from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models
from ..schemas import ProjectCreate, ProjectUpdate
from ..repositories.project_repository import ProjectRepository

class ProjectService:
    def __init__(self, db: Session):
        self.db = db
        self.project_repo = ProjectRepository(db)

    def create_project(self, project: ProjectCreate, current_user: models.User):
        project_data = project.dict()
        project_data["owner_id"] = current_user.id
        return self.project_repo.create_project(project_data)

    def get_projects(self, current_user: models.User, skip: int = 0, limit: int = 100):
        return self.project_repo.get_projects_by_owner(current_user.id, skip, limit)

    def get_project(self, project_id: int, current_user: models.User):
        project = self.project_repo.get_project(project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Projet non trouvé")
        if project.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Accès non autorisé")
        return project

    def get_project_with_stats(self, project_id: int, current_user: models.User):
        project = self.get_project(project_id, current_user)
        stats = self.project_repo.get_project_stats(project_id)
        if not stats:
            raise HTTPException(status_code=404, detail="Projet non trouvé")
        project_dict = project.__dict__.copy()
        project_dict.update(stats)
        return project_dict

    def update_project(self, project_id: int, project_update: ProjectUpdate, current_user: models.User):
        self.get_project(project_id, current_user)  # validation owner
        updated = self.project_repo.update_project(project_id, project_update)
        if not updated:
            raise HTTPException(status_code=404, detail="Projet non trouvé")
        return updated

    def delete_project(self, project_id: int, current_user: models.User):
        self.get_project(project_id, current_user)  # validation owner
        deleted = self.project_repo.delete_project(project_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Projet non trouvé")
        return deleted

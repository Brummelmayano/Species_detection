from sqlalchemy.orm import Session
from typing import List
from .. import models

class DetectionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_detection(self, detection_data: dict):
        db_detection = models.Detection(**detection_data)
        self.db.add(db_detection)
        self.db.commit()
        self.db.refresh(db_detection)
        return db_detection

    def get_detections_by_image(self, image_id: int):
        return self.db.query(models.Detection).filter(models.Detection.image_id == image_id).all()

    def get_detection(self, detection_id: int):
        return self.db.query(models.Detection).filter(models.Detection.id == detection_id).first()

    def bulk_create_detections(self, detections_data: List[dict]):
        db_detections = [models.Detection(**data) for data in detections_data]
        self.db.add_all(db_detections)
        self.db.commit()
        for detection in db_detections:
            self.db.refresh(detection)
        return db_detections

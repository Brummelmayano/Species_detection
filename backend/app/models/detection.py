from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..database import Base

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    species_name = Column(String, nullable=False)
    confidence_score = Column(Float, nullable=False)
    bbox_x_min = Column(Float, nullable=False)
    bbox_y_min = Column(Float, nullable=False)
    bbox_x_max = Column(Float, nullable=False)
    bbox_y_max = Column(Float, nullable=False)
    bbox_width = Column(Float)
    bbox_height = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    validated = Column(String, default="pending")  # pending, validated, rejected
    validated_by_id = Column(Integer, ForeignKey("users.id"))
    notes = Column(Text)

    # Relations
    image = relationship("Image", back_populates="detections")
    validated_by = relationship("User")
from app import db
from sqlalchemy import (
    Column, String, Integer, String, DateTime, Boolean, func
)

class MarcaModel(db.Model):
    __tablename__ = 'marcas'
    marca_id = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
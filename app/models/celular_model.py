from app import db
from sqlalchemy import (
    Column, Text, Integer, String, Float, DateTime, Boolean, func
)

class CelularModel(db.Model):
    __tablename__ = 'celulares'
    celular_id = Column(Integer, primary_key=True)
    marca_id = Column(Integer, db.ForeignKey('marcas.marca_id'))
    marca = db.relationship('MarcaModel')
    descripcion = Column(Text)
    codigo = Column(String(6))
    stock = Column(String(4))
    precio_online = Column(Float(5,2))
    precio_normal = Column(Float(5,2), nullable=False)
    imagen = Column(Text)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
from app import db
from sqlalchemy import (
    Column, String, Integer, Text, String, Boolean, DateTime, func
)

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'
    usuario_id = Column(Integer, primary_key=True)
    nombres = Column(String(45), nullable=False)
    apellidos = Column(String(45), nullable=False)
    direccion = Column(Text)
    email = Column(String(320), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    password_salt = Column(String(60), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
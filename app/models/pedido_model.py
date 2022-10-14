from app import db
from sqlalchemy import (
    Column, Float, Integer, Boolean, DateTime, func
)

class PedidoModel(db.Model):
    __tablename__ = 'pedidos'
    pedido_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, db.ForeignKey('usuarios.usuario_id'))
    usuario = db.relationship('UsuarioModel')
    monto_total = Column(Float)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
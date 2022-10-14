from app import db
from sqlalchemy import (
    Column, Float, Integer, DateTime, func
)
from sqlalchemy.dialects.mysql import TINYINT

class DetallePedidoModel(db.Model):
    __tablename__ = 'detalle_pedidos'
    detalle_pedido_id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, db.ForeignKey('pedidos.pedido_id'))
    pedido = db.relationship('PedidoModel')
    celular_id = Column(Integer, db.ForeignKey('celulares.celular_id'))
    celular = db.relationship('CelularModel')
    cantidad = Column(TINYINT)
    precio = Column(Float(5, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
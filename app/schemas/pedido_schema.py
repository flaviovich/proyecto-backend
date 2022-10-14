from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario

class PedidoSchema(Schema):
    pedido_id = fields.Integer(dump_only=True)
    usuario_id = fields.Integer(required=True, validate=campo_necesario)
    monto_total = fields.Float(required=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

order_schema = PedidoSchema()
orders_schema = PedidoSchema(many=True)

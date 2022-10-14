from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario

class DetallePedidoSchema(Schema):
    usuario_id = fields.Integer(dump_only=True)
    nombres = fields.String(required=True, validate=campo_necesario)
    apellidos = fields.String(required=True, validate=campo_necesario)
    direccion = fields.String(dump_only=True)
    email = fields.String(required=True, validate=campo_necesario)
    password = fields.String(required=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

order_detail_schema = DetallePedidoSchema()
# order_details_schema = DetallePedidoSchema(many=True)

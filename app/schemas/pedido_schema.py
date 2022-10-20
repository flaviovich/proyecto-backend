from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario
from app.schemas.usuario_schema import UsuarioSchema

class PedidoSchema(Schema):
    pedido_id = fields.Integer(dump_only=True)
    usuario_id = fields.Integer(required=True, load_only=True, validate=campo_necesario)
    usuario = fields.Nested(UsuarioSchema)
    monto_total = fields.Float(required=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

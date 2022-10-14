from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario

class CelularSchema(Schema):
    celular_id = fields.Integer(dump_only=True)
    marca_id = fields.Integer(required=True, validate=campo_necesario)
    descripcion = fields.String(required=True, validate=campo_necesario)
    codigo = fields.String(required=True, validate=campo_necesario)
    stock = fields.String(required=True, validate=campo_necesario)
    precio_online = fields.Float()
    precio_normal = fields.Float(required=True, validate=campo_necesario)
    imagen = fields.String(required=True, validate=campo_necesario)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

cell_schema = CelularSchema()
cells_schema = CelularSchema(many=True)

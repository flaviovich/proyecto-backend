from ast import dump
from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario
from app.schemas.marca_schema import MarcaSchema

class CelularSchema(Schema):
    celular_id = fields.Integer(dump_only=True)
    marca_id = fields.Integer(required=True, load_only=True, validate=campo_necesario)
    marca = fields.Nested(MarcaSchema)
    descripcion = fields.String(required=True, validate=campo_necesario)
    codigo = fields.String(required=True, validate=campo_necesario)
    stock = fields.String(required=True, validate=campo_necesario)
    precio_online = fields.Float()
    precio_normal = fields.Float(required=True, validate=campo_necesario)
    imagen = fields.String(required=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

#cell_schema = CelularSchema()
#cells_schema = CelularSchema(many=True)

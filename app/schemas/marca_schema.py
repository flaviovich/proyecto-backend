from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario

class MarcaSchema(Schema):
    marca_id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime(load_only=True)
    updated_at = fields.DateTime(load_only=True)

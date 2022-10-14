from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario

class MarcaSchema(Schema):
    marca_id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=campo_necesario)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

brand_schema = MarcaSchema()
brands_schema = MarcaSchema(many=True)

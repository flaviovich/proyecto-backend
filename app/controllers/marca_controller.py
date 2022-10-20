from app import db
from app.models.marca_model import MarcaModel
from app.schemas.marca_schema import MarcaSchema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

class MarcaController():
    def __init__(self):
        self.brand_schema = MarcaSchema()
        self.brands_schema = MarcaSchema(many=True)

    def getAll(self):
        marcas = MarcaModel.query.all()
        result = self.brands_schema.dump(marcas)

        return result, 200

    @jwt_required()
    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400

        try:
            data = self.brand_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422

        marca = MarcaModel(**data)
        db.session.add(marca)
        db.session.commit()
        result = self.brand_schema.dump(marca)

        return result, 201
    
    @jwt_required()
    def update(self, id, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
            
        try:
            data = self.brand_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        brand = MarcaModel.query.filter_by(marca_id=id).first()
        brand.nombre = data['nombre']
        db.session.commit()
        result = self.brand_schema.dump(brand)
        return result, 201

    @jwt_required()
    def delete(self, id):
        brand = MarcaModel.query.filter_by(marca_id=id).first()
        brand.estado = False
        db.session.commit()
        result = self.brand_schema.dump(brand)
        return result, 201

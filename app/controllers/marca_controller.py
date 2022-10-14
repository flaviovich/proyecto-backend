from app import db
from app.models.marca_model import MarcaModel
from app.schemas.marca_schema import brand_schema, brands_schema
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required

class MarcaController():
    def getAll(self):
        marcas = MarcaModel.query.all()
        result = brands_schema.dump(marcas)

        return result, 200

    @jwt_required()
    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400

        try:
            data = brand_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422

        marca = MarcaModel(**data)
        db.session.add(marca)
        db.session.commit()
        result = brand_schema.dump(marca)

        return result, 201
    
    @jwt_required()
    def update(self, id, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
            
        try:
            data = brand_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        brand = MarcaModel.query.filter_by(marca_id=id).first()
        brand.nombre = data['nombre']
        db.session.commit()
        result = brand_schema.dump(brand)
        return result, 201

    @jwt_required()
    def delete(self, id):
        brand = MarcaModel.query.filter_by(marca_id=id).first()
        db.session.delete(brand)
        db.session.commit()
        result = brand_schema.dump(brand)
        return result, 204

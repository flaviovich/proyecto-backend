from app.models.celular_model import CelularModel
from app.schemas.celular_schema import CelularSchema
from marshmallow import ValidationError
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class CelularController():
    def __init__(self):
        self.cell_schema = CelularSchema()
        self.cells_schema = CelularSchema(many=True)

    @jwt_required()
    def getAll(self):
        products = CelularModel.query.all()
        result = self.cells_schema.dump(products)
        return result, 200

    @jwt_required()
    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400

        try:
            data = self.cell_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        cell = CelularModel(**data)
        db.session.add(cell)
        db.session.commit()
        result = self.cell_schema.dump(cell)
        return result, 201

    @jwt_required()
    def update(self, id, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
            
        try:
            data = self.cell_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        cell = CelularModel.query.filter_by(celular_id=id).first()
        cell.marca_id = data['marca_id']
        cell.descripcion = data['descripcion']
        cell.codigo = data['codigo']
        cell.stock = data['stock']
        cell.precio_online = data['precio_online']
        cell.precio_normal = data['precio_normal']
        cell.imagen = data['imagen']
        db.session.commit()
        result = self.cell_schema.dump(cell)
        return result, 201

    @jwt_required()
    def delete(self, id):
        cell = CelularModel.query.filter_by(celular_id=id).first()
        cell.estado = False
        db.session.commit()
        result = self.cell_schema.dump(cell)
        return result, 201

    def getTodos(self):
        cells = CelularModel.query.filter_by(estado=True).all()
        result = self.cells_schema.dump(cells)
        return result, 200

    def getById(self, id):
        cell = CelularModel.query.filter_by(celular_id=id).first()
        print(cell)
        result = self.cell_schema.dump(cell)
        return result, 200

    def getByName(self, nombre):
        cells = CelularModel.query.filter(CelularModel.descripcion.like(f"%{nombre}%")).all()
        result = self.cells_schema.dump(cells)
        return result, 200

    def getByMarca(self, marca_id):
        cells = CelularModel.query.filter_by(marca_id=marca_id).all()
        result = self.cells_schema.dump(cells)
        return result, 200

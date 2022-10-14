from app.models.pedido_model import PedidoModel
from app.schemas.pedido_schema import order_schema, orders_schema
from marshmallow import ValidationError
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class PedidoController():
    @jwt_required()
    def getAll(self):
        orders = PedidoModel.query.all()
        result = orders_schema.dump(orders)
        return result, 200

    @jwt_required()
    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
        try:
            data = order_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        order = PedidoModel(**data)
        db.session.add(order)
        db.session.commit()
        result = order_schema.dump(order)
        return result, 201
    
    @jwt_required()
    def getById(self, pedido_id):
        order = PedidoModel.query.filter_by(pedido_id=pedido_id).first()
        result = order_schema.dump(order)
        return result, 200

    @jwt_required()
    def getByEstado(self, categoria_id):
        user_id = get_jwt_identity()
        if user_id == 2:
            orders = PedidoModel.query.filter_by(categoriaId=categoria_id).all()
            result = order_schema.dump(orders)
            return result, 200
        return {"message": "El usuario no tiene permisos."}, 403

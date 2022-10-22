from app.models.pedido_model import PedidoModel
from app.schemas.pedido_schema import PedidoSchema
from marshmallow import ValidationError
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class PedidoController():
    def __init__(self):
        self.order_schema = PedidoSchema()
        self.orders_schema = PedidoSchema(many=True)

    @jwt_required()
    def getAll(self):
        usuario_id = get_jwt_identity()
        orders = PedidoModel.query.filter_by(usuario_id=usuario_id).all()
        result = self.orders_schema.dump(orders)
        return result, 200

    @jwt_required()
    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
        try:
            data = self.order_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        order = PedidoModel(**data)
        db.session.add(order)
        db.session.commit()
        result = self.order_schema.dump(order)
        return result, 201

    @jwt_required()
    def update(self, id, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
            
        try:
            data = self.order_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        usuario_id = get_jwt_identity()
        order = PedidoModel.query.filter_by(usuario_id=usuario_id, pedido_id=id).first()
        order.monto_total = data['monto_total']
        db.session.commit()
        result = self.order_schema.dump(order)
        return result, 201

    @jwt_required()
    def delete(self, id):
        usuario_id = get_jwt_identity()
        order = PedidoModel.query.filter_by(usuario_id=usuario_id, pedido_id=id).first()
        order.estado = False
        db.session.commit()
        result = self.order_schema.dump(order)
        return result, 201

    @jwt_required()
    def getById(self, id):
        order = PedidoModel.query.filter_by(pedido_id=id).first()
        result = self.order_schema.dump(order)
        return result, 200

    @jwt_required()
    def getByEstado(self, categoria_id):
            orders = PedidoModel.query.filter_by(categoriaId=categoria_id).all()
            result = self.order_schema.dump(orders)
            return result, 200

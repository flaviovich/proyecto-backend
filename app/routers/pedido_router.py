from app import app
from flask import request
from app.controllers.pedido_controller import PedidoController

@app.route("/pedidos", methods=['GET'])
def listarPedidos():
    orders = PedidoController()
    return orders.getAll()

@app.route("/pedidos", methods=['POST'])
def crearPedido():
    json_input = request.get_json()
    result = PedidoController()
    return result.post(json_input)

@app.route("/pedidos/<int:id>", methods=['PUT'])
def actualizarPedido(id):
    order = PedidoController()
    json_input = request.get_json()
    return order.update(id, json_input)

@app.route("/pedidos/<int:id>", methods=['DELETE'])
def eliminarPedido(id):
    order = PedidoController()
    return order.delete(id)

@app.route("/pedidos/id/<int:id>", methods=['GET'])
def pedidoPorId(id):
    pedido = PedidoController()
    return pedido.getById(id)

@app.route("/pedidos/situacion/<string:situacion>", methods=['GET'])
def pedidoPorSituacion(situacion):
    pedido = PedidoController()
    return pedido.getByEstado(situacion)

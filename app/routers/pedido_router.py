from app import app
from flask import request
from app.controllers.pedido_controller import PedidoController

@app.route("/pedidos/", methods=['GET', 'POST'])
def pedidos():
    # sourcery skip: inline-immediately-returned-variable, remove-unnecessary-else
    if request.method == 'GET':
        orders = PedidoController().getAll()
        return orders
    else:
        json_input = request.get_json()
        result = PedidoController().post(json_input)
        return result

@app.route("/pedidos/id/<int:pedido_id>", methods=['GET'])
def pedidosPorId(pedido_id):
    pedido = PedidoController()
    return pedido.getById(pedido_id)

@app.route("/pedidos/get_by_estado/<int:estado>", methods=['GET'])
def pedidosPorEstado(estado_id):
    pedido = PedidoController()
    return pedido.getByEstado(estado_id)

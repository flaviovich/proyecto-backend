from app import app
from flask import request
from app.controllers.celular_controller import CelularController

@app.route("/admin/celulares", methods=['GET'])
def listarCelulares():
    celulares = CelularController()
    return celulares.getAll()

@app.route("/admin/celulares", methods=['POST'])
def crearCelular():
    json_input = request.get_json()
    result = CelularController()
    return result.post(json_input)

@app.route("/admin/celulares/<int:id>", methods=['PUT'])
def actualizarCelular(id):
    celular = CelularController()
    json_input = request.get_json()
    return celular.update(id, json_input)

@app.route("/admin/celulares/<int:id>", methods=['DELETE'])
def eliminarCelular(id):
    celular = CelularController()
    return celular.delete(id)

@app.route("/celulares", methods=['GET'])
def celularTodos():
    if 'id' in request.args:
        return celularPorId(request.args['id'])
    elif 'nombre' in request.args:
        return celularPorNombre(request.args['nombre'])
    celulares = CelularController()
    return celulares.getTodos()

@app.route("/celulares/<int:id>", methods=['GET'])
def celularPorId(id):
    celular = CelularController()
    return celular.getById(id)

@app.route("/celulares/<string:nombre>", methods=['GET'])
def celularPorNombre(nombre):
    celulares = CelularController()
    return celulares.getByName(nombre)

@app.route("/celulares/marca/<int:id>", methods=['GET'])
def celularPorMarca(id):
    celulares = CelularController()
    return celulares.getByMarca(id)

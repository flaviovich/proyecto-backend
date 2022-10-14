from app import app
from flask import request
from app.controllers.celular_controller import CelularController

@app.route("/celulares", methods=['GET'])
def listarCelulares():  # sourcery skip: inline-immediately-returned-variable
    celulares = CelularController().getAll()
    return celulares

@app.route("/celular", methods=['POST'])
def crear():  # sourcery skip: inline-immediately-returned-variable
    json_input = request.get_json()
    result = CelularController().post(json_input)
    return result

@app.route("/celular/<int:id>", methods=['PUT'])
def actualizar(id):
    celular = CelularController()
    json_input = request.get_json()
    return celular.update(id,json_input)

@app.route("/celular/<int:id>", methods=['DELETE'])
def eliminar(id):
    celular = CelularController()
    return celular.delete(id)

@app.route("/celulares/id/<int:id>", methods=['GET'])
def celularPorId(id):
    celular = CelularController()
    return celular.getById(id)

@app.route("/celulares/marca/<int:id>", methods=['GET'])
def celularesPorMarca(id):
    celulares = CelularController()
    return celulares.getByMarca(id)

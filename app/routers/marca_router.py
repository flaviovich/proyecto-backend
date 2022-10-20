from app import app
from flask import request
from app.controllers.marca_controller import MarcaController

@app.route("/admin/marcas", methods=['GET'])
def listarMarcas():
    marcas = MarcaController()
    return marcas.getAll()

@app.route("/admin/marcas", methods=['POST'])
def crearMarca():
    json_input = request.get_json()
    result = MarcaController()
    return result.post(json_input)

@app.route("/admin/marcas/<int:id>", methods=['PUT'])
def actualizarMarca(id):
    marca = MarcaController()
    json_input = request.get_json()
    return marca.update(id, json_input)

@app.route("/admin/marcas/<int:id>", methods=['DELETE'])
def eliminarMarca(id):
    marca = MarcaController()
    return marca.delete(id)

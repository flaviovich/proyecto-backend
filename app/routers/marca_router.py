from app import app
from flask import request
from app.controllers.marca_controller import MarcaController

@app.route("/marcas", methods=['GET'])
def listar():
    return MarcaController().getAll()

@app.route("/marca", methods=['POST'])
def crear():
    json_input = request.get_json()
    return MarcaController().post(json_input)

@app.route("/marca/<int:id>", methods=['PUT'])
def actualizar(id):
    marca = MarcaController()
    json_input = request.get_json()
    return marca.update(id, json_input)
    
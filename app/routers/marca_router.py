from app import app
from flask import request
from app.controllers.marca_controller import MarcaController

@app.route("/marcas/", methods=['GET', 'POST'])
def marcas():
    # sourcery skip: inline-immediately-returned-variable, remove-unnecessary-else
    if request.method == 'GET':
        brands = MarcaController().getAll()
        return brands
    else:
        json_input = request.get_json()
        result = MarcaController().post(json_input)
        return result

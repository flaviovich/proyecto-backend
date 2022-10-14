from app import app
from app.controllers.usuario_controller import UsuarioController
from flask import request

@app.route('/registro', methods=['POST'])
def registrarUsuario():  # sourcery skip: inline-immediately-returned-variable
    json_input = request.get_json()
    usuario = UsuarioController().signUp(json_input)
    return usuario
    
@app.route('/login', methods=['POST'])
def iniciarSesion():  # sourcery skip: inline-immediately-returned-variable
    json_input = request.get_json()
    usuario = UsuarioController().signIn(json_input)
    return usuario

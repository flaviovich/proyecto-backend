from app import app
from app.controllers.usuario_controller import UsuarioController
from flask import request

@app.route("/admin/usuarios", methods=['GET'])
def listarUsuarios():
    usuarios = UsuarioController()
    return usuarios.getAll()

@app.route("/admin/usuarios/<int:id>", methods=['PUT'])
def actualizarUsuario(id):
    usuario = UsuarioController()
    json_input = request.get_json()
    return usuario.update(id, json_input)

@app.route("/admin/usuarios/<int:id>", methods=['DELETE'])
def eliminarUsuario(id):
    usuario = UsuarioController()
    return usuario.delete(id)

@app.route('/registro', methods=['POST'])
def registrarUsuario():
    json_input = request.get_json()
    usuario = UsuarioController()
    return usuario.signUp(json_input)
    
@app.route('/login', methods=['POST'])
def iniciarSesion():
    json_input = request.get_json()
    usuario = UsuarioController()
    return usuario.signIn(json_input)
    
@app.route('/reset', methods=['PUT'])
def resetPassword():
    json_input = request.get_json()
    usuario = UsuarioController()
    return usuario.reset(json_input)

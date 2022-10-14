from app.schemas.usuario_schema import user_schema, auth_schema
from marshmallow import ValidationError
from app.models.usuario_model import UsuarioModel
from app import db
import bcrypt
from flask_jwt_extended import create_access_token

class UsuarioController():
    def signUp(self, json_input):
        if not json_input:
            return {"message": "Datos de usuario no encontrado"}, 400

        try:
            data = user_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422

        email = self.__searchUser(data['email'])
        if email:
            return {"message": "El usuario ya existe."}, 400

        # encriptamos la contraseña
        try:
            hashe = bytes(data['password'], 'utf-8')
            salt = bcrypt.gensalt()
            passwordHashed = bcrypt.hashpw(hashe, salt)
            saltDecoded = salt.decode('utf-8')
            passwordHashedDecoded = passwordHashed.decode('utf-8')

            usuario = UsuarioModel(
                nombres = data['nombres'],
                apellidos = data['apellidos'],
                direccion = data['direccion'],
                email = data['email'],
                password = passwordHashedDecoded,
                password_salt = saltDecoded
            )
            db.session.add(usuario)
            db.session.commit()
            result = user_schema.dump(usuario)
        except Exception as e:
            return {"message": f'{e}'}, 500

        return result, 201

    def signIn(self, json_input):
        if not json_input:
            return {"message": "Datos de usuario no encontrado"}, 400
        
        try:
            data = auth_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        user = self.__searchUser(data['email'])
        if not user:
            return {"message": "Credenciales incorrectas"}, 400
    
        try:
            password = bytes(data['password'], 'utf-8')
            salt = bytes(user.password_salt, 'utf-8')
            passwordHashed = bcrypt.hashpw(password, salt)
            passwordHashedDecoded = passwordHashed.decode('utf-8')
            access_token = create_access_token(identity=user.usuario_id)
        except ValidationError as e:
            return {"message": f'{e}'}, 500
        
        if passwordHashedDecoded == user.password:
            return {"access token": access_token}, 200
        return {"message": "Credenciales incorrectas"}, 400 

    def __searchUser(self, email):
        # sourcery skip: inline-immediately-returned-variable
        usuario = UsuarioModel.query.filter_by(email=email).first()

        return usuario

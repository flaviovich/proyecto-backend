from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from logging import (
    basicConfig, 
    DEBUG, 
    FileHandler, 
    StreamHandler
)
import os
from datetime import timedelta

basicConfig(
    level=DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[FileHandler('flask.log'), StreamHandler()]
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI_REMOTE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "c0d1Go"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
jwt = JWTManager(app)

@app.route("/")
def index():
    return f"Server working on port={os.getenv('FLASK_RUN_PORT')}"

from app import routers

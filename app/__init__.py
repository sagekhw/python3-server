# import os
# import sys
# import json
# import pymysql
# import urllib 
from flask import Flask
from flask_jwt_extended import *
from flask_jwt_extended import JWTManager
from .controller.YaroController import *
from .controller.SimbaController import *
from .controller.AuthController import *
from app.config.AppConfig import *

app = Flask(__name__)


#### JWT ####
app.config["JWT_SECRET_KEY"] = FlaskConfig.JWT_SECRET_KEY
jwt = JWTManager(app)
"""
# jwt = JWTManager()
# jwt.init_app(app)
"""
app.register_blueprint(yaro)
app.register_blueprint(simba)
app.register_blueprint(auth)

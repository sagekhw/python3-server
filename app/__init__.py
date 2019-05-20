import os
import sys
import json
import pymysql
import urllib 
from flask import Flask

app = Flask(__name__, template_folder="templates")

from app.main.main import main as main
from app.main.auth import auth as auth

#print(__name__)
app.register_blueprint(main)
app.register_blueprint(auth)
 
#login_manager = LoginManager()
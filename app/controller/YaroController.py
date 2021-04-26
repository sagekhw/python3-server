import json
# from flask import Blueprint, request, render_template, flash, redirect, url_for, session
# from flask import current_app as current_app
from flask import Blueprint
from app.config.sql_db.orm.crud import *
from app.entities.user import user
from app.repositories.userRepository import *
from app.services.userService import *
from flask_jwt_extended import *
from flask_jwt_extended import jwt_required


yaro = Blueprint('YaroController', __name__ ,url_prefix='/yaro')

user_service = userService()

@yaro.route('/a', methods=['GET'])
@jwt_required()
def a():
    # return "aaaaa"
    return user_service.read_all()

@yaro.route('/a1', methods=['GET'])
def a1():
    # return "a1 a1 a1 a1 a1"
    return user_service.read_all()

@yaro.route('/b', methods=['GET'])
def b():
    x = user()
    table_name = 'user'
    id_name = 'user_id'
    id = 1
    query = f"SELECT * FROM {table_name} where {id_name} = {id}"
    temp = x.findBySQL(query)
    jsonString = json.dumps(temp[0])
    return str(jsonString)


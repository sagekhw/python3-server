from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
from app.models.User import *
import json

auth = Blueprint('auth', __name__, url_prefix='/')

base_meta = {'baseUrl':'http://0.0.0.0/'} 

@auth.route('/login', methods=['GET'])
def GET_login():
    testData = 'testData array'
    return render_template('auth/login.html', testDataHtml=testData, base_Meta=base_meta)

@auth.route('/login', methods=['POST'])
def POST_login():
    id          = request.form.get('id')
    password    = request.form.get('password')
    print("ID : ",id," PW : ",password)
    check_Interface(id,password)
    return render_template('auth/login.html', base_Meta=base_meta)

def check_Interface(UserID,UserPassword):
    #UserID,UserPassword
    print("check_Interface")
    a = user(TableName='User',UserID='sagekhw')
    print(a.select(a,option='one'))
    print(a.select(option=a.db_switch(queryCustom='all')))
    print(a.select(option=a.db_switch(queryCustom='count')))
    #a.switch(queryCustom='count')
    #a.switch()
    return "result"

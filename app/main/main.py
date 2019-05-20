import json
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
from app.models.User import *

'''
#Test db query
a = user(tableName='User')
print(a.select(a))
'''
main = Blueprint('main', __name__, url_prefix='/')

base_meta = {'baseUrl':'http://0.0.0.0/'} 

@main.route('/main', methods=['GET'])
def index():
    testData = 'testData array'
    return render_template('main/index.html', testDataHtml=testData, base_Meta=base_meta)

@main.route('/about', methods=['GET'])
def about():
    testData = 'testData array'
    return render_template('main/about.html', testDataHtml=testData, base_Meta=base_meta)

@main.route('/contact', methods=['GET'])
def contact():
    testData = 'testData array'
    return render_template('main/contact.html', testDataHtml=testData, base_Meta=base_meta)

@main.route('/login1', methods=['GET'])
def login():
    testData = 'testData array'
    return render_template('auth/login.html', testDataHtml=testData, base_Meta=base_meta)
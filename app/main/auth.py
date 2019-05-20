from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

#from . import db
auth = Blueprint('auth', __name__, url_prefix='/')

base_meta = {'baseUrl':'http://0.0.0.0/'} 
'''
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
    db_connect = db.db_init()
    cur     = db_connect.cursor(db.default_cursor)
    result  = cur.execute("SELECT * FROM User WHERE UserID = '"+UserID+"' AND UserPassword='"+UserPassword+"'")
    rv      = cur.fetchall()
    if result == 1:
        print("rv_userID : ",rv[0]['UserID'],"  |  rv_password : ",rv[0]['UserPassword'],
              "  |  rv_UserAuthority : ",rv[0]['UserAuthority'],"  /   result : ",result)
    else :
        print("DO NOT Search")

    cur.close()
    return result
'''
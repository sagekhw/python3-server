from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from flask import current_app as current_app
from app.models.User import *
import json

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
    result = check_Interface(id,password)
    return render_template('auth/loginDone.html', base_Meta=base_meta, testDataHtml = result)
'''
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        testData = 'testData array'
        return render_template('auth/login.html', testDataHtml=testData, base_Meta=base_meta)
    
    if request.method == 'POST':
        print("Login POST")
        id          = request.form.get('id')
        password    = request.form.get('password')
        print("ID : ",id," PW : ",password)
        result = check_Interface(id,password)
        print("login result : ",result)
        if(result == True):
            print(request.form['id'])
            session['username'] = request.form['id']
            #return redirect(url_for('index'))
            return render_template('auth/loginDone.html', base_Meta=base_meta, testDataHtml = result)
        else:
            return redirect(url_for('login'))

@auth.route('/logout', methods=['GET'])
def logout():
    # remove the username from the session if its there
    session.pop('username', None)
    return render_template('auth/login.html', base_Meta=base_meta)

@auth.route('/signup', methods=['GET'])
def GET_signup():    
    return render_template('auth/signup.html', base_Meta=base_meta, method=['GET'])

@auth.route('/signup', methods=['POST'])
def POST_signup():
    id          = request.form.get('id')
    password    = request.form.get('password')
    authority    = request.form.get('authority')
    print("*******************************************")
    #print("ID : ",id," PW : ",password," Auth : ",authority)
    check_Interface(id,password)
    insert_User(id,password,authority)
    
    return render_template('auth/login.html', base_Meta=base_meta, method=['GET'])

@auth.route('/windowOpen2', methods=['GET'])
def GET_login1():
    testData = 'testData array'
    return render_template('auth/windowOpen2.html', testDataHtml=testData, base_Meta=base_meta)

@auth.route('/admin', methods=['POST'])
def GET_admin():
    testData = 'testData array'
    return render_template('auth/admin_main.html', testDataHtml=testData, base_Meta=base_meta)

@auth.route('/UserListAll', methods=['GET'])
def GET_UserListAll():
    testData = 'testData array'
    a = user(TableName='User')
    result = a.select(a,option='All')
    return render_template('auth/admin_main.html', users=result, base_Meta=base_meta)

def check_Interface(UserID,UserPassword=None):
    #UserID,UserPassword
    #print("check_Interface")
    a = user(TableName='User',UserID=UserID)
    result = a.select(a,option='one')

    print("Login input : ",UserID,UserPassword)

    #print(a.select(option=a.db_switch(queryCustom='all')))
    #print(a.select(option=a.db_switch(queryCustom='count')))
    #a.switch(queryCustom='count')
    #a.switch()
    print(result)
    print(type(result))
    print(len(result))

    if(type(result) == tuple ):
        print("result tuple type")
    
    if(type(result) == list ):
        print("result list type")

    if(len(result) == 0 ):
        print("result false")
        return False
    else:
        print("result true")
        return True


def insert_User(userid=None,password=None,auth=None):
    a = user(TableName='User',UserID=userid,UserPassword=password,UserAuthority=auth)
    print(a.db_insert(a,option='one'))
    

from app.config.sql_db.db import *

def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')



def DB_SQL_READ(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        db_connect = db_init()
        cur = db_connect.cursor(pymysql.cursors.DictCursor)
        func(query)                               # 매개변수로 받은 함수를 호출
        cur.execute(query)
        rv = cur.fetchall()
        cur.close()
        return wrapper    

def findByAllTest(self):
    db_connect = db_init()
    cur = db_connect.cursor(pymysql.cursors.DictCursor)
    query="SELECT * FROM user limit 10"
    cur.execute(query)
    rv = cur.fetchall()
    cur.close()
    return rv

import pymysql
import json

with open('server_info.json', mode='rt', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    #print(json_data)
    
    
conns = []
default_cursor = pymysql.cursors.DictCursor
def db_init():
    dbconn = pymysql.connect(
        host=json_data['production']['DATABASES']['default']['HOST']        ,
        port=json_data['production']['DATABASES']['default']['PORT']        , 
        user=json_data['production']['DATABASES']['default']['USER']        , 
        passwd=json_data['production']['DATABASES']['default']['PASSWORD']  , 
        db=json_data['production']['DATABASES']['default']['NAME']          ,
        charset='utf8'                                                      ,
        autocommit=True    
    )

    conns.append(dbconn)

    return conns.pop()

def init_db_query(query):
        db_connect = db_init()
        cur = db_connect.cursor(pymysql.cursors.DictCursor)
        cur.execute(query)
        rv = cur.fetchall()
        cur.close()
        return rv
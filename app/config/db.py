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
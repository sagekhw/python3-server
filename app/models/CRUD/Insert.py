from app.config.db import *

class insert:
    options = []

    def __init__(self):
        pass
    '''
    def addOption(self, option):
        options.append(option)
    '''
    
    def db_insert(self,model=None,option=None):
        db_connect = db_init()
        cur     = db_connect.cursor(pymysql.cursors.DictCursor)
        print("DB_INSERT")
        if(option==None or option=="one"):
            query="INSERT INTO "+ model.TableName +" (UserID, UserPassword, UserAuthority) VALUES ('"+model.UserID+"','"+model.UserPassword+"','"+model.UserAuthority+"')"            
        elif(option == "1"):
            query="SELECT * FROM "+model.TableName +" where UserID like '"+model.UserID+"'"
        else:
            if(model==None):
                query=option
            else:
                print("Nothing query")
        cur.execute(query)
        rv      = cur.fetchall()
        cur.close()
        return rv


   
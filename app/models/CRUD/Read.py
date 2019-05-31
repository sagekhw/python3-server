from app.config.db import *

class read:
    options = []

    def __init__(self):
        pass
    '''
    def addOption(self, option):
        options.append(option)
    '''
    def select(self,model=None,option=None):
        db_connect = db_init()
        cur     = db_connect.cursor(pymysql.cursors.DictCursor)

        if(option==None or option=="All"):
            query="SELECT * FROM "+model.TableName
        elif(option == "one"):
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


   
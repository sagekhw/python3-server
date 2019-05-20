from app.config.db import *

class read:
    options = []

    def __init__(self):
        pass
    '''
    def addOption(self, option):
        options.append(option)
    '''
    def select(self,model,option=None):
        '''
        for x in options:
            print(x)
        '''
        db_connect = db_init()
        cur     = db_connect.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM "+model.tableName)
        rv      = cur.fetchall()
        cur.close()
        return rv

   
from .insert import insert
from .read import read

class crud(insert,read):
    def __init__(self):
        pass

    def init_db_query(self,query):
        db_connect = db_init()
        cur = db_connect.cursor(pymysql.cursors.DictCursor)
        cur.execute(query)
        rv = cur.fetchall()
        cur.close()
        return rv

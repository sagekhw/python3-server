from app.config.sql_db.orm.crud import crud
from app.config.sql_db.orm.read import *

class user(crud):
    
    def __init__(self,email=None,password=None,role=None):
        self.table_name = self.__class__.__name__
        self.email = email
        self.password = password
        self.role = role
        
    def a(self):
        print("a ",self.__class__.__name__)

    # def findByAll(self):
    #     return crud.findByAll(self,self.table_name)

    # def findByOne(self):
    #     table_name = self.table_name
    #     id_name = 'user_id'
    #     id = 1
    #     query = f"SELECT email FROM {table_name} where {id_name} = {id}"
    #     return crud.findBySQL(self,query)

    # def findBySQL(self,query):
    #     return crud.findBySQL(self,query)

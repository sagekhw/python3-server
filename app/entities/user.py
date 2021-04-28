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

  

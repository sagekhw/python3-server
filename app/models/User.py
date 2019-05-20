
from app.models.CRUD.CRUD import *



class user(crud):

    def __init__(self,tableName=None):
        self.tableName = tableName    

    def view_aa(self):
        print("aa")    

from app.models.CRUD.CRUD import *



class user(crud):

    def __init__(self,TableName=None,UserID=None,UserPassword=None,UserAuthority=None):
        self.TableName      = TableName
        self.UserID         = UserID
        self.UserPassword   = UserPassword
        self.UserAuthority  = UserAuthority    

    def view_aa(self):
        print("aa")

    def db_switch(self,queryCustom=None):
        choices = {
            'all': 'SELECT * FROM User'
            ,'count': 'SELECT count(*) FROM User'
            ,'defualt':'defualt'
            }
        result = choices.get(queryCustom,'defualt')
        #print("result : ",result)
        return result
        
        
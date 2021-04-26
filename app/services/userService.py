from app.config.sql_db.orm.crud import *
from app.repositories.userRepository import *
from app.entities.user import *

repo = userRepository()

class userService:
    def __init__(self):
        pass
    
    def read_all(self):
        temp = repo.findByAll()
        res = json.dumps(temp,indent=2)
        return res
    

    def readByEmailandPassword(self,email,password):
        try:
            temp = repo.findByEmail_Password(email,password)
        except Exception as e:
            print(e)
            return "False"
        else:
            if(not temp):
                return "nothing"
            else:
                res = temp
                return res
        finally:
            pass
    
    def insert_by_register(self,userObj):
        try:
            temp = repo.insertAuthSql(userObj.email,userObj.password,userObj.role)
        except Exception as e:
            print(e)
            return False
        else:
            return True
        finally:
            pass
        
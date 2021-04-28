from app.config.sql_db.orm.crud import *
from app.repositories.userRepository import *
from app.entities.user import *
from flask import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity,get_jwt,get_jti)
import bcrypt

repo = userRepository()

class userService:
    def __init__(self):
        pass
    
    def read_all(self):
        temp = repo.findByAll()
        res = json.dumps(temp,indent=2)
        return res
    

    def readByEmail(self,email):
        try:
            temp = repo.findByEmail(email)
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

    def readByEmailandPassword(self,email,password):
        try:
            temp = repo.findByEmail_Password(email,password)
        except Exception as e:
            print(e)
            return "False"
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
    
    def user_register(self,user):
        if(user.role == 'role_user' or user.role == 'role_admin'):
            
            encrypted_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
            user.password = encrypted_password.decode("utf-8")
            result = self.insert_by_register(user)

            if result:
                return "success"
            else:
                return "false"
        else:
        	return jsonify(
        		result = "Invalid Params!"
        		)

    def login_check(self,user_email,user_password):
        temp = self.readByEmail(user_email)

        if(temp == "nothing" or temp == "False"):
            return jsonify(
                result = "Invalid Params!"
                )
        else:
            input_role = temp[0]['role']
            if(not input_role):
                return "false"
            
            pw = temp[0]['password']
            if(not bcrypt.checkpw(user_password.encode("utf-8"), pw.encode("utf-8"))):
                return "false"

            additional_claims = {"role": f"{input_role}"}
            return jsonify(result = "success",
                # 검증된 경우, access 토큰 반환
                access_token = create_access_token(identity = user_email,
                                                additional_claims=additional_claims,
                                                expires_delta = False)
            )	
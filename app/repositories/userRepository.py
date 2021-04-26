from app.config.sql_db.orm.crud import *
from app.config.sql_db.orm.read import *
from app.config.sql_db.orm.insert import *
from app.entities.user import *


class userRepository(user):
    def __init__(self):
        self.table_name = 'user'
        self.str_email = 'email'
        self.str_password = 'password'
        self.str_role = 'role'

    def findByAll(self):
        return crud.findByAll(self,self.table_name)

    def findByEmail(self,email):
        query = f"SELECT * FROM {self.table_name} where {self.str_email} = '{email}'"
        return crud.findBySQL(self,query)

    def findByEmail_Password(self,email,password):
        query = (
            f"SELECT * FROM {self.table_name} " + 
            f"where {self.str_email} = '{email}' and { self.str_password} = '{password}'"
            )
        return crud.findBySQL(self,query)

    def insertAuthSql(self,email,password,role):
        query = (
            f"INSERT INTO {self.table_name} " +
            f" ({self.str_email},{ self.str_password},{self.str_role}) " + 
            f"VALUES ('{email}','{password}','{role}')"
            )
        return crud.InsertBySQL(self,query)
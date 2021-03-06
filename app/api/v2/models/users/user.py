"""This module creates user model and its operations"""
# standard imports
from datetime import datetime

# local imports
from ..models import BaseModel


class User(BaseModel):
    """Class that represent a user"""
    def __init__(self):
        self.created_date = datetime.now().strftime("%Y, %m, %d")
        super().__init__()

    def create_user(self, first_name, last_name, email, user_name, password):
        """Method that creates user while assignind role user"""
        sql = """WITH users AS(
            INSERT INTO users(
                first_name, last_name,email,
                user_name, password,
                created_at) VALUES(%s, %s, %s, %s, %s, %s) RETURNING user_id
            ), roles AS(SELECT role_id FROM roles WHERE role_name='user')
            INSERT INTO user_roles(role_id, user_id)
            SELECT roles.role_id, users.user_id FROM roles, users RETURNING id;"""
        return self.cud_operations(
            sql, (
                first_name, last_name,
                email, user_name, password,
                self.created_date))

    def get_all_users(self):
        """Method that gets all users"""
        sql = "SELECT * FROM users;"
        rows = self.read_items(sql)
        users_list = []
        for _, users in enumerate(rows):
            user_id, first_name, last_name,\
                email, user_name, password, created_at = users
            accounts = dict(
                Id=user_id,
                First_name=first_name.upper(),
                Last_name=last_name.upper(),
                Email=email,
                User_name=user_name,
                Password=password,
                Created_date=str(created_at)
            )
            users_list.append(accounts)
        return users_list

    def get_user_by_user_id(self, user_id):
        """Method for get a specific user"""
        sql = "SELECT * FROM users WHERE user_id=%s;"
        return self.cud_operations(sql, (user_id,))

    def get_user_by_user_name_email(self, user_name, email):
        """Method for get a specific user"""
        sql = "SELECT user_name, email FROM users WHERE user_name=%s OR email=%s;"
        return self.cud_operations(sql, (user_name, email))

    def get_user_password_and_id(self, user_name):
        """Method for get a specific user"""
        sql = "SELECT user_id, password FROM users WHERE user_name=%s;"
        return self.cud_operations(sql, (user_name,))

    def update_user(self, email, password, user_id):
        """Method that updates specific user"""
        sql = """UPDATE users SET email=(%s), password=(%s), user_role=(%s)
                WHERE user_id=(%s) RETURNING user_id;"""
        return self.cud_operations(sql, (email, password, user_id))

    def get_user_role_id(self, user_name):
        sql= """SELECT s.role_id 
                FROM user_roles s, users u
                WHERE s.user_id=u.user_id AND u.user_name=%s;"""
        return self.cud_operations(sql, (user_name, ))
        
    def get_role_name_by_user_id(self, user_id):
        sql="""SELECT r.role_name
                FROM user_roles u, roles r
                WHERE r.role_id=u.role_id AND user_id=%s;"""
        return self.cud_operations(sql, (user_id, ))
    
    

    def delete_user(self, user_id):
        """Method for delete specific user"""
        sql = "DELETE FROM users WHERE user_id=(%s) RETURNING user_id;"
        return self.cud_operations(sql, (user_id,))

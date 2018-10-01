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
        """Method that creates user"""
        sql = """INSERT INTO users(first_name, last_name,
                email, user_name, password,
                created_date) VALUES(%s, %s, %s, %s, %s, %s) RETURNING user_id;"""
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
                email, user_name, user_role, authenticated,\
                password, created_date = users
            accounts = dict(
                Id=user_id,
                First_name=first_name.upper(),
                Last_name=last_name.upper(),
                Email=email,
                User_name=user_name,
                User_role=user_role,
                Authenticated=authenticated,
                Password=password,
                Created_date=str(created_date)
            )
            users_list.append(accounts)
        return users_list

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

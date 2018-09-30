"""This module creates user model and its operations"""
# standard imports
from datetime import datetime
# local imports
from app.db_setups import create_dev_db_tables


class UserModel:
    """This class methods for users endpoints"""
    def __init__(
            self,
            user_id=None,
            first_name=None,
            last_name=None,
            email=None,
            user_name=None,
            user_role=None,
            password=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_name = user_name
        self.user_role = user_role
        self.password = password
        self.created_date = datetime.now().strftime("%Y, %m, %d")
        self.conn = create_dev_db_tables()

    def post_user(self):
        """Method for create users"""
        sql = """INSERT INTO users(
            first_name, last_name,
            email, user_name,
            password,
            created_date) VALUES(%s, %s, %s, %s, %s, %s);"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (
            self.first_name,
            self.last_name,
            self.email,
            self.user_name,
            self.password,
            self.created_date))
        self.conn.commit()
        self.conn.close()

    def get_all_users(self):
        """Method for get all users"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users;")
        self.conn.close()
        return cursor.fetchall()

    def get_user_by_user_role(self, user_role):
        """Method for get a specific users"""
        sql = "SELECT * FROM users WHERE user_role=%s;"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_role,))
        self.conn.close()
        return cursor.fetchall()

    def get_user_by_user_id(self, user_id):
        """Method for get a specific user"""
        sql = "SELECT * FROM users WHERE user_id=%s;"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id,))
        self.conn.close()
        return cursor.fetchone()

    def put_user_role(self, user_id):
        """Method for update specific user"""
        sql = "UPDATE users SET user_role=(%s) WHERE user_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id,))
        self.conn.commit()
        self.conn.close()

    def put_user_password(self, user_id):
        """Method for update specific user"""
        sql = "UPDATE users SET password=(%s) WHERE user_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id,))
        self.conn.commit()
        self.conn.close()

    def put_user_name(self, user_id):
        """Method for update specific user"""
        sql = "UPDATE users SET user_name=(%s) WHERE user_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id,))
        self.conn.commit()
        self.conn.close()

    def put_user_email(self, user_id):
        """Method for update specific user"""
        sql = "UPDATE users SET email=(%s) WHERE user_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id,))
        self.conn.commit()
        self.conn.close()

    def delete_user(self, user_id):
        """Method for delete specific user"""
        sql = "DELETE FROM users WHERE user_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id,))
        self.commit()
        self.close()

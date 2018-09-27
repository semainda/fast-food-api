"""This module creates categories model and its operations"""
# local imports
from app.db_setups import create_dev_db_tables


class CategoriesModel:
    """This class methods for category endpoints"""
    #def __init__(self):

    def post_category(self, cat_name):
        """Method for create category"""
        conn = create_dev_db_tables()
        sql = """INSERT INTO categories(cat_name) VALUES(%s);"""
        cursor = conn.cursor()
        cursor.execute(sql, (cat_name,))
        conn.commit()
        cursor.close()

    def get_all_categories(self):
        """Method for get all categories"""
        conn = create_dev_db_tables()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories;")
        data = cursor.fetchall()
        cursor.close()
        return data
        

    def get_category(self, cat_id):
        """Method for get a specific category"""
        conn = create_dev_db_tables()
        sql = "SELECT cat_name FROM categories WHERE cat_id=%s;"
        cursor = conn.cursor()
        cursor.execute(sql, (cat_id,))
        data = cursor.fetchone()
        cursor.close()
        return data
        

    def put_category(self, cat_name, cat_id):
        """Method for update specific category"""
        conn = create_dev_db_tables()
        sql = "UPDATE categories SET cat_name=(%s) WHERE cat_id=(%s);"
        cursor = conn.cursor()
        cursor.execute(sql, (cat_name, cat_id))
        conn.commit()
        cursor.close()

    def delete_category(self, cat_id):
        """Method for delete specific category"""
        conn = create_dev_db_tables()
        sql = "DELETE FROM categories WHERE cat_id=(%s);"
        cursor = conn.cursor()
        cursor.execute(sql, (cat_id,))
        conn.commit()
        cursor.close()

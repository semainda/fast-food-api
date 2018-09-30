"""Module that creates category model"""
# local imports
from app.db_config.db_setups import DatabaseOperations

class Category():
    """
    Class that represents a category of the meal

    The following attributes of a category are stored in this table:
        category id
        category name
    """
    def __init__(self):
        self.conn = DatabaseOperations().db_con()

    def create_category(self, cat_name):
        """Method that create category"""
        sql = """INSERT INTO categories(cat_name) VALUES(%s);"""
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(sql, (cat_name,))
        self.conn.close()
    
    def get_category_by_id(self, cat_id):
        """Method that returns a specific category"""
        sql = "SELECT cat_name FROM categories WHERE cat_id=%s;"
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(sql, (cat_id,))
                row = curr.fetchone()
        self.conn.close()
        return row

    def get_category_by_name(self, cat_name):
        """Method that returns a specific category"""
        sql = "SELECT cat_name FROM categories WHERE cat_name=%s;"
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(sql, (cat_name,))
                row = curr.fetchone()
        self.conn.close()
        return row

    def get_all_categories(self):
        """Method that returns a list of categories"""
        sql = "SELECT * FROM categories;"
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(sql)
                rows = curr.fetchall()
        self.conn.close()
        categories = []
        for index, items in enumerate(rows):
            cat_id, cat_name = items
            menu_category=dict(
                cat_id = cat_id,
                cat_name=cat_name
                )
            categories.append(menu_category)
        return categories

    def update_category(self, cat_name, cat_id):
        """Method that update specific category"""
        sql = "UPDATE categories SET cat_name=(%s) WHERE cat_id=(%s) RETURNING cat_id;"
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(sql, (cat_name, cat_id))
                row = curr.fetchone()
        self.conn.close()
        return row

    def delete_category(self, cat_id):
        """Method that delete specific category"""
        sql = "DELETE FROM categories WHERE cat_id=(%s) RETURNING cat_id;"
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(sql, (cat_id,))
                row = curr.fetchone()
        self.conn.close()
        return row
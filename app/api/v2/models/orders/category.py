"""Module that creates category model"""
# local imports
from ..models import BaseModel


class Category(BaseModel):
    """
    Class that represents a category of the meal

    The following attributes of a category are stored in this table:
        category id
        category name
    """
    def __init__(self):
        super().__init__()

    def create_category(self, cat_name):
        """Method that create category"""
        sql = "INSERT INTO categories(cat_name) VALUES(%s) RETURNING cat_name;"
        return self.cud_operations(sql, (cat_name, ))

    def get_category_by_id(self, cat_id):
        """Method that returns a specific category"""
        sql = "SELECT cat_name FROM categories WHERE cat_id=%s;"
        return self.cud_operations(sql, (cat_id,))

    def get_category_by_name(self, cat_name):
        """Method that returns a specific category"""
        sql = "SELECT cat_id FROM categories WHERE cat_name=%s;"
        return self.cud_operations(sql, (cat_name,))

    def get_all_categories(self):
        """Method that returns a list of categories"""
        sql = "SELECT * FROM categories;"
        rows = self.read_items(sql)
        categories = []
        for _, items in enumerate(rows):
            cat_id, cat_name = items
            category = dict(
                Id=cat_id,
                Name=cat_name.upper()
            )
            categories.append(category)
        return categories

    def update_category(self, cat_name, cat_id):
        """Method that update specific category"""
        sql = "UPDATE categories SET cat_name=(%s)\
            WHERE cat_id=(%s) RETURNING cat_name;"
        return self.cud_operations(sql, (cat_name, cat_id))

    def delete_category(self, cat_id):
        """Method that delete specific category"""
        sql = "DELETE FROM categories WHERE cat_id=(%s) RETURNING cat_name CASCADE;"
        return self.cud_operations(sql, (cat_id,))

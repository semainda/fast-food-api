"""Module that creates meal model"""
# local imports
from ..models import BaseModel


class Meal(BaseModel):
    """This class methods for meals endpoints"""
    def __init__(self):
        super().__init__()

    def create_meal(self, meal_name, cat_id, description, price):
        """Method that creates meal"""
        sql = """INSERT INTO meals(meal_name, cat_id, description, price)
        VALUES(%s, %s, %s, %s) RETURNING meal_id;"""
        return self.cud_operations(sql, (
            meal_name, cat_id, description, price))

    def get_meal_by_name(self, meal_name):
        """Method that returns existing meal name"""
        sql = "SELECT meal_name FROM meals WHERE meal_name=%s;"
        return self.cud_operations(sql, (meal_name,))

    def get_meal_by_id(self, meal_id):
        """Method that returns a specific meal"""
        sql = """SELECT meal_name, description, price , c.cat_name
                FROM meals m, categories c
                WHERE m.meal_id=%s AND m.cat_id=c.cat_id;"""
        return self.cud_operations(sql, (meal_id,))

    def get_all_meals(self):
        """Method that returns a list of meals available"""
        sql = """SELECT meal_id, meal_name, description, price , c.cat_name
                FROM meals m, categories c WHERE m.cat_id=c.cat_id;"""
        menu = self.read_items(sql)
        menu_list = []
        for _, items in enumerate(menu):
            meal_id, meal_name, desc, price, cat_name = items
            display = dict(
                Id=meal_id,
                Name=meal_name.upper(),
                Price="TZS " + str(price),
                Description=desc.upper(),
                Category=cat_name.upper()
                )
            menu_list.append(display)
        return menu_list

    def update_all_meal_entries(
            self, meal_name, cat_id, description, price, meal_id):
        """Method that update all meal entries"""
        sql = """UPDATE meals SET meal_name=(%s), cat_id=(%s),
                description=(%s), price=(%s)
                WHERE meal_id=(%s) RETURNING meal_id;"""
        return self.cud_operations(
            sql, (meal_name, cat_id, description, price, meal_id)
            )

    def delete_meal(self, meal_id):
        """Method that delete meal"""
        sql = "DELETE FROM meals WHERE meal_id=(%s) RETURNING meal_id;"
        return self.cud_operations(sql, (meal_id,))

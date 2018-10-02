"""This module creates orders model and its operations"""
# standard imports
from datetime import datetime

# local imports
from .order_status import status
from ..models import BaseModel


class Order(BaseModel):
    """This class methods for orders endpoints"""
    def __init__(self):
        super().__init__()
        self.created_date = str(datetime.now().strftime("%Y-%m-%d"))

    def create_order(self, user_id, delivery_address, meal_id, quantity, description=None):
        """Method for create order"""
        sql = """WITH ordered AS(
            INSERT INTO orders(user_id, delivery_address, description, created_date)
            VALUES(%s, %s, %s, %s) RETURNING order_id)
            INSERT INTO orders_items 
            SELECT ordered.order_id, %s, %s FROM ordered RETURNING order_id;"""
        self.cud_operations(sql, (user_id, delivery_address, description, self.created_date, meal_id, quantity))

    





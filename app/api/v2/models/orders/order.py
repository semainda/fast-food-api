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

    def create_order(self, user_id, delivery_address, meal_id, quantity, description=""):
        """Method for create order"""
        sql = """WITH ordered AS(
            INSERT INTO orders(user_id, delivery_address, description, created_date)
            VALUES(%s, %s, %s, %s) RETURNING order_id)
            INSERT INTO orders_items 
            SELECT ordered.order_id, %s, %s FROM ordered RETURNING order_id;"""
        self.cud_operations(sql, (
            user_id, delivery_address,
            description, self.created_date,
            meal_id, quantity))

    def get_all_orders(self):
        """Method that returns a list of orders"""
        sql = """SELECT o.order_id, u.first_name, u.last_name, m.meal_name,
                i.quantity, o.description, o.status, o.delivery_address,
                o.created_date,o. delivery_time
                FROM orders o, users u, meals m, orders_items i 
                WHERE o.user_id=u.user_id AND i.meal_id=m.meal_id
                AND o.order_id=i.order_id;"""
        rows = self.read_items(sql)
        orders = []
        for _, items in enumerate(rows):
            order_id, first_name,\
            last_name, meal_name, quantity,\
            description, status, delivery_address,\
            created_date, delivery_time = items
            order = dict(
                Id=order_id,
                User=first_name + " " + last_name,
                Meal=meal_name,
                Quantity=quantity,
                Description=description,
                Status=status,
                Adress=delivery_address,
                Created=str(created_date),
                Delivery=str(delivery_time))
            orders.append(order)
        return orders





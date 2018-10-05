"""This module creates orders model and its operations"""
# standard imports
from datetime import datetime

# local imports
from ..models import BaseModel


class Order(BaseModel):
    """This class methods for orders endpoints"""
    def __init__(self):
        super().__init__()
        self.created_date = str(datetime.now().strftime("%Y-%m-%d"))

    def create_order(
        self, user_id, delivery_address,
        meal_id, quantity, description=""):
        """Method for create order"""
        sql ="""WITH orders AS(
                INSERT INTO orders(user_id,
                    delivery_address, description,
                    created_date) VALUES(%s, %s, %s, %s) RETURNING order_id
                ),
                status AS(
                    SELECT status_id FROM status WHERE status_name='New')
                INSERT INTO order_status(order_id, status_id)
                SELECT orders.order_id, status.status_id FROM orders, status
                INSERT INTO orders_items 
                SELECT orders.order_id, %s, %s
                FROM orders RETURNING order_id;"""
        self.cud_operations(sql, (
            user_id, delivery_address,
            description, self.created_date,
            meal_id, quantity))

    def get_all_orders(self):
        """Method that returns a list of orders"""
        sql = """SELECT o.order_id, u.first_name, u.last_name, m.meal_name,
                i.quantity, o.description, o.status, o.delivery_address,
                o.created_date, o.delivery_time
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

    def get_all_user_orders(self, user_id):
        """Method that returns a list user order history"""
        sql = """SELECT o.order_id, u.first_name, u.last_name, m.meal_name,
                i.quantity, o.description, o.status, o.delivery_address,
                o.created_date,o.delivery_time
                FROM orders o, users u, meals m, orders_items i 
                WHERE o.user_id=u.user_id AND i.meal_id=m.meal_id
                AND o.order_id=i.order_id AND i.user_id=%s;"""
        rows = self.read_items(sql, (user_id, ))
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

    def get_order_by_id(self, order_id):
        """Method that returns a specific category"""
        sql = """SELECT o.order_id, u.first_name, u.last_name, m.meal_name,
                i.quantity, o.description, o.status, o.delivery_address,
                o.created_date,o. delivery_time
                FROM orders o, users u, meals m, orders_items i 
                WHERE o.user_id=u.user_id AND i.meal_id=m.meal_id
                AND o.order_id=i.order_id AND o.order_id=%s;"""
        return self.cud_operations(sql, (order_id,))
    
    def get_user_order_by_id(self, order_id, user_id):
        """Method that returns a specific category"""
        sql = """SELECT o.order_id, u.first_name, u.last_name, m.meal_name,
                i.quantity, o.description, o.status, o.delivery_address,
                o.created_date,o. delivery_time
                FROM orders o, users u, meals m, orders_items i 
                WHERE o.user_id=u.user_id AND i.meal_id=m.meal_id
                AND o.order_id=i.order_id AND o.order_id=%s, i.user_id=%s;"""
        return self.cud_operations(sql, (order_id, user_id))

    def get_order_by_status(self, status):
        """Method that returns a specific category"""
        sql = """SELECT o.order_id, u.first_name, u.last_name, m.meal_name,
                i.quantity, o.description, o.status, o.delivery_address,
                o.created_date,o. delivery_time
                FROM orders o, users u, meals m, orders_items i 
                WHERE o.user_id=u.user_id AND i.meal_id=m.meal_id
                AND o.order_id=i.order_id AND o.status=%s;"""
        return self.cud_operations(sql, (status,))
    
    def update_order_status(self, order_id, status):
        """Method that update order status"""
        sql = """UPDATE order_status SET status_id =%s
                    WHERE order_id=%s RETURNING order_id;"""
        return self.cud_operations(sql, (status, order_id))
    
    def get_all_status(self):
        sql = """SELECT * FROM status"""
        return self.read_items(sql)
        



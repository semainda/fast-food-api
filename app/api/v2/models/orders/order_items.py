"""This module creates orders items model and its operations"""
# local imports
from app.db_setups import create_dev_db_tables


class OrdersItemsModel:
    """This class methods for orders items endpoints"""
    def __init__(
            self, order_id=None, meal_id=None,
            quantity=None, description=None):
        self.order_id = order_id
        self.meal_id = meal_id
        self.quantity = quantity
        self.description = description
        self.conn = create_dev_db_tables()

    def post_order_items(self):
        """Method for create orders items"""
        sql = """INSERT INTO orders_items(
            order_id, meal_id, quantity,
            description) VALUES(%s, %s, %s, %s);"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (
            self.order_id, self.meal_id,
            self.quantity, self.description))
        self.conn.commit()
        self.conn.close()

    def get_all_orders_items(self):
        """Method for get all orders items"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders_items;")
        self.conn.close()
        return cursor.fetchall()

    def get_order_items(self, order_id):
        """Method for get a specific order items"""
        sql = "SELECT * FROM orders_items WHERE order_id=%s;"
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.conn.close()
        return cursor.fetchall()

    def put_order_item_quantity(self, order_id):
        """Method for update specific order items"""
        sql = "UPDATE orders_items SET quantity=(%s) WHERE order_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.conn.commit()
        self.conn.close()

    def put_order_item_description(self, order_id):
        """Method for update specific order items"""
        sql = "UPDATE orders_items SET description=(%s) WHERE order_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.conn.commit()
        self.conn.close()

    def delete_order_items(self, order_id):
        """Method for delete specific order items"""
        sql = "DELETE FROM orders_items WHERE order_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.commit()
        self.close()

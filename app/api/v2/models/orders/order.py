"""This module creates orders model and its operations"""
# standard imports
from datetime import datetime
# local imports
from app.db_setups import create_dev_db_tables


class OrdersModel:
    """This class methods for orders endpoints"""
    def __init__(self, user_id=None, delivery_address=None):
        self.created_date = datetime.now().strftime("%Y, %m, %d")
        self.delivery_address = delivery_address
        self.conn = create_dev_db_tables()

    def post_order(self):
        """Method for create order"""
        sql = """INSERT INTO orderss(
            user_id,
            delivery_address,
            created_date) VALUES(%s, %s, %s);"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (
            self.user_id,
            self.delivery_address,
            self.created_date))
        self.conn.commit()
        self.conn.close()

    def get_all_orders(self):
        """Method for get all orders"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders;")
        self.conn.close()
        return cursor.fetchall()

    def get_order(self, order_id):
        """Method for get a specific order"""
        sql = """SELECT * FROM orders WHERE order_id=%s;"""
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.conn.close()
        return cursor.fetchone()

    def put_order_delivery_address(self, order_id):
        """Method for update specific order address"""
        sql = "UPDATE orders SET delivery_address=(%s) WHERE order_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.conn.commit()
        self.conn.close()

    def put_order_status(self, order_id):
        """Method for update specific order status"""
        sql = "UPDATE orders SET status=(%s) WHERE order_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.conn.commit()
        self.conn.close()

    def delete_order(self, order_id):
        """Method for delete specific order"""
        sql = "DELETE FROM orders WHERE order_id=(%s);"
        cursor = self.conn.cursor()
        cursor.execute(sql, (order_id,))
        self.commit()
        self.close()

"""Module that holds all acceptable order status"""
# local imports
from ..models import BaseModel


class Status(BaseModel):
    """This class methods for meals endpoints"""
    def __init__(self):
        super().__init__()

    def create_order_status(self, status_name, st_code):
        """Method that creates order status"""
        sql = """INSERT INTO order_status(name, code)
        VALUES(%s, %s) RETURNING name;"""
        return self.cud_operations(sql, (status_name, st_code))

    def get_order_status_by_name(self, status_name):
        """Method that returns existing order status name"""
        sql = "SELECT name FROM order_status WHERE name=%s;"
        return self.cud_operations(sql, (status_name,))

    def get_order_status_by_id(self, status_id):
        """Method that returns a specific meal"""
        sql = """SELECT code, name FROM order_status WHERE id=%s;"""
        return self.cud_operations(sql, (status_id,))

    def get_all_order_status(self):
        """Method that returns a list of meals available"""
        sql = """SELECT * FROM order_status;"""
        status = self.read_items(sql)
        status_list = []
        for _, items in enumerate(status):
            status_id, code, status_name = items
            status_dict = dict(
                Id=status_id,
                Name=status_name.upper(),
                Code=code
                )
            status_list.append(status_dict)
        return status_list

    def update_order_status(self, status_name, code, status_id):
        """Method that update all order status entries"""
        sql = """UPDATE order_status SET name=(%s), code=(%s),
                WHERE id=(%s) RETURNING id;"""
        return self.cud_operations(
            sql, (status_name, code, status_id)
            )

    def delete_order_status(self, status_id):
        """Method that delete order status"""
        sql = "DELETE FROM order_status WHERE id=(%s) RETURNING id;"
        return self.cud_operations(sql, (status_id,))

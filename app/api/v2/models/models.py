"""Module that creates model for all models class"""
from app.db_config.db_setups import DatabaseOperations


class BaseModel:
    """
        Class that offers crud operations
    """
    def __init__(self):
        self.conn = DatabaseOperations().db_con()

    def read_items(self, query=None, val=None):
        """
            Method that performs read operations to return rows
        """
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(query, val)
                rows = curr.fetchall()
        self.conn.close()
        return rows

    def cud_operations(self, query=None, val=None):
        """
            Method that performs create,
            update and delete operation to return a row
        """
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(query, val)
                row = curr.fetchone()
        # self.conn.close()
        return row

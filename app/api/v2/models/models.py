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
            Method that performs read operations to return effected rows
        """
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(query, val)
                rows = curr.fetchall()
        self.conn.close()
        data_items = []
        for _, items in enumerate(rows):
            cat_id, cat_name = items
            category = dict(
                cat_id=cat_id,
                cat_name=cat_name
                )
            data_items.append(category)
        return data_items

    def cud_operations(self, query=None, val=None):
        """
            Method that performs create,
            update and delete operation to return the effected row
        """
        with self.conn:
            with self.conn.cursor() as curr:
                curr.execute(query, val)
                row = curr.fetchone()
        self.conn.close()
        return row

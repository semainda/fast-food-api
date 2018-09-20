"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask import request
from flask_restful import Resource

# Local imports
from .models import ORDERS_DATA
from .validators import OrderItemsValodator

DATE = datetime.now().strftime("%B %d, %Y")
STATUS_CODE = 0  # received


class Orders(Resource):
    """Class that creates orders and list all orders"""
    def get(self):
        """Orders requesting"""
        if ORDERS_DATA:
            return {"orders": ORDERS_DATA}, 200
        return {"Message": "There is no order that exist"}, 404

    def post(self):
        """Order creation"""
        json_data = request.get_json(force=True, silent=True)

        if json_data:
            if OrderItemsValodator(json_data['item']).text_validator():
                if OrderItemsValodator(
                        json_data['description']).text_validator():
                    # if OrderItemsValodator(
                    # json_data['quantity']).number_validator():
                        ORDERS_DATA.append(
                            dict(
                                id=len(ORDERS_DATA) + 1,
                                item=json_data["item"],
                                description=json_data["description"],
                                quantity=json_data["quantity"],
                                order_date=DATE,
                                status=STATUS_CODE
                            )
                        )
                        return {"Message": "Order created successful"}, 201
                    # return {"Message": "Invalid order quantity"}, 400
                return {"Message": "Invalid order description"}, 400
            return {"Message": "Invalid order item"}, 400
        return {'Message': "You can not create empty order"}, 200

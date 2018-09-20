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


class OrderActivity(Resource):
    """Fetch, update and delete specific order by supplying order id"""
    def get(self, order_id):
        """Requesting a specific order otherwise return 404"""
        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        if order:
            return {"Order": order[0]}, 200
        return {"Message":
                "Order with ID = {} does not exist".format(order_id)}, 404

    def put(self, order_id):
        """Update specific order to return appropriate status code"""

        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        json_data = request.get_json(force=True, silent=True)

        if order:
            if json_data:
                # if OrderItemsValodator(json_data["status"]).text_validator():
                order[0]["status"] = json_data["status"]
                return {"Message": "Order status updated"}, 200
                # return {"Message": "Invalid order item"}, 400
            return {
                "Message":
                "You can not update an order with empty entries"}, 400
        return {
            "Message":
            "Order with ID = {} does not exist".format(order_id)}, 404

    def delete(self, order_id):
        """Delete specific order to return 200 or 404"""
        order = [order for order in ORDERS_DATA if order['id'] == order_id]
        if order:
            ORDERS_DATA.remove(order[0])
            return {
                "Message":
                "Order with an ID = {} deleted".format(order_id)}, 200
        return {
            "Message":
            "Order with an ID = {} does not exist".format(order_id)}, 404

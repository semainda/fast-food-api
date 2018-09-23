"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask import request
from flask_restful import Resource

# Local imports
from ..models.models import ORDERS_DATA
from ..utils.validators import OrderItemsValodator

DATE = datetime.now().strftime("%B %d, %Y")
DEFAULT_STATUS_CODE = 3  # received

STATUS = {"Accepted": 1, "Declined": 0, "Completed": 2}


class Orders(Resource):
    """Class that creates orders and list all orders"""
    def get(self):
        """Orders requesting"""
        if ORDERS_DATA:
            return {"Orders": ORDERS_DATA}, 200
        return {
            "Message": "Nothing Found",
            "Description": "Orders not created yet",
            "Status": "NOT FOUND"}, 404

    def post(self):
        """Order creation"""
        json_data = request.get_json(force=True, silent=True)
        if not json_data:
            return {
                "Message": "Empty Order Not Allowed",
                "Description": "Order can not be created",
                "Status": "NOT ALLOWED"}, 200

        if not OrderItemsValodator(json_data['item']).is_string_validator():
            return {
                "Message": "Invalid Order Item",
                "Description": "Order can not be created",
                "Status": "BAD REQUEST"}, 400

        if not OrderItemsValodator(
                json_data['description']).is_string_validator():
            return {
                "Message": "Invalid Order Description",
                "Description": "Order can not be created",
                "Status": "BAD REQUEST"}, 400

        if not OrderItemsValodator(json_data['quantity']).is_int_validator():
            return {
                "Message": "Invalid Order Quantity",
                "Description":
                "Order with quantity value <= 0 or string can not be created",
                "Status": "BAD REQUEST"}, 400

        ORDERS_DATA.append(
            dict(
                id=len(ORDERS_DATA) + 1,
                item=json_data["item"],
                description=json_data["description"],
                quantity=json_data["quantity"],
                create_date=DATE,
                status=DEFAULT_STATUS_CODE,
                last_updated=DATE
            )
        )
        return {
            "Message": "Created",
            "Description": "Order Successful Created",
            "Status": "RECEIVED"}, 200


class OrderActivity(Resource):
    """Fetch, update and delete specific order by supplying order id"""
    def get(self, order_id):
        """Requesting a specific order otherwise return 404"""
        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        if order:
            return {
                "Order": order[0]}, 200
        return {
            "Message": "Invalid Order ID",
            "Description":
            "Order with ID = {} does not exist".format(order_id),
            "Status": "NOT FOUND"}, 404

    def put(self, order_id):
        """Update specific order to return appropriate status code"""
        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        json_data = request.get_json(force=True, silent=True)

        if not order:
            return {
                "Message": "Invalid Order ID",
                "Description":
                "Order with ID = {} does not exist".format(order_id),
                "Status": "NOT FOUND"}, 404

        if not json_data:
            return {
                "Message": "Empty Status Not Allowed",
                "Description":
                "Order with ID = {}, Status can not be updated"
                .format(order_id),
                "Status": "BAD REQUEST"}, 400

        if not OrderItemsValodator(json_data["status"]).is_string_validator():
            return {
                "Message": "Invalid Order Status",
                "Description":
                "Order with ID = {}, Status can not be updated"
                .format(order_id),
                "Status": "BAD REQUEST"}, 400

        if not json_data["status"] in [key for key in STATUS]:
            return {
                "Message": "Undefined Order Status",
                "Description":
                "Order with ID = {}, Status can not be updated"
                .format(order_id),
                "Status": "UNDEFINED"}

        order[0]["status"] = STATUS[json_data["status"]]
        return {
            "Message": "Status Updated",
            "Description":
            "Order with ID = {}, Status updated".format(order_id),
            "Status": "UPDATED"}, 200

    def delete(self, order_id):
        """Delete specific order to return 200 or 404"""
        order = [order for order in ORDERS_DATA if order['id'] == order_id]
        if order:
            ORDERS_DATA.remove(order[0])
            return {
                "Message": "Order Deleted",
                "Description":
                "Order with ID = {} Deleted Successful".format(order_id),
                "Status": "DELETED"}, 200

        return {
            "Message": "Invalid Order ID",
            "Description":
            "Order with ID = {} does not exist".format(order_id),
            "Status": "NOT FOUND"}, 404

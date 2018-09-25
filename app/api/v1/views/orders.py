"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask import request
from flask_restful import Resource, reqparse

# Local imports
from ..models.models import ORDERS_DATA
from ..utils.order_validators import post_validators
from ..responses.orders_responses import PostResponse, PutRespose, DeleteResponse, GetResponse

DATE = datetime.now().strftime("%B %d, %Y")
DEFAULT_STATUS_CODE = 3  # received

STATUS = {"Accepted": 1, "Declined": 0, "Completed": 2}


class Orders(Resource):
    """Class that creates orders and list all orders"""
    def get(self):
        """Orders requesting"""
        if ORDERS_DATA:
            return GetResponse(ORDERS_DATA).get_exist_orders_response()
        return GetResponse().get_unexist_orders_response()

    def post(self):
        """Order creation"""
        parser = reqparse.RequestParser()
        parser.add_argument("item", required=True, help="Order item can't be empty")
        parser.add_argument("description", required=True, help="Order description can't be empty")
        parser.add_argument("quantity", type=int, required=True, help="Order quantity can't be empty ")
        data_parsed = parser.parse_args()
        item = data_parsed["item"]
        description = data_parsed["description"]
        quantity = data_parsed["quantity"]
        output = post_validators.order_str_data_validator(item=item, description=description)
        if output[0]:
            if post_validators.order_int_data_validator(quantity):
                ORDERS_DATA.append(
                dict(
                    id=len(ORDERS_DATA) + 1,
                    item=item,
                    description=description,
                    quantity=quantity,
                    create_date=DATE,
                    status=DEFAULT_STATUS_CODE,
                    last_updated=DATE
                    )
                )
                return PostResponse().post_order_with_valid_entries_both_type_and_value_response()
            return PostResponse().post_order_with_invalid_quantity_type_and_value_response()
        return PostResponse(output[1]).post_order_with_invalid_item_description_type_and_value_response()


class OrderActivity(Resource):
    """Fetch, update and delete specific order by supplying order id"""
    def get(self, order_id):
        """Requesting a specific order otherwise return 404"""
        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        if order:
            return GetResponse().get_order_with_valid_id_response()
        return GetResponse(order_id).get_order_with_invalid_id_response()

    def put(self, order_id):
        """Update specific order to return appropriate status code"""
        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        parser = reqparse.RequestParser()
        parser.add_argument("status", required=True, help="Status can't be empty")
        data_parsed = parser.parse_args()
        status = data_parsed["status"]

        if order:
            if status  in [key for key in STATUS]:
                order[0]["status"] = STATUS[status]
                return PutRespose(order_id).put_order_with_valid_status_response()
            return PutRespose(order_id).put_order_with_undefined_status_response()
        return PutRespose(order_id).put_order_with_invalid_id_response()

    def delete(self, order_id):
        """Delete specific order to return 200 or 404"""
        order = [order for order in ORDERS_DATA if order['id'] == order_id]
        if order:
            ORDERS_DATA.remove(order[0])
            return DeleteResponse(order_id).delete_order_with_valid_id_response()
        return DeleteResponse(order_id).delete_order_with_invalid_id_response()

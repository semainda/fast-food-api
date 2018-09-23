"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask import request
from flask_restful import Resource

# Local imports
from ..models.models import ORDERS_DATA
from ..utils.validators import OrderItemsValodator
from ..responses.orders_responses import GetResponse,\
    PostResponse, PutRespose, DeleteResponse

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
        json_data = request.get_json(force=True, silent=True)
        if not json_data:
            return PostResponse().post_order_with_empty_entries_response()
        if not OrderItemsValodator(json_data['item']).is_string_validator():
            return PostResponse().\
                post_order_with_invalid_item_type_and_value_response()
        if not OrderItemsValodator(
                json_data['description']).is_string_validator():
            return PostResponse().\
                post_order_with_invalid_description_type_and_value_response()
        if not OrderItemsValodator(json_data['quantity']).is_int_validator():
            return PostResponse().\
                post_order_with_invalid_quantity_type_and_value_response()
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
        return PostResponse().\
            post_order_with_valid_entries_both_type_and_value_response()


class OrderActivity(Resource):
    """Fetch, update and delete specific order by supplying order id"""
    def get(self, order_id):
        """Requesting a specific order otherwise return 404"""
        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        if order:
            return GetResponse(order[0]).get_order_with_valid_id_response()
        return GetResponse(order_id).get_order_with_invalid_id_response()

    def put(self, order_id):
        """Update specific order to return appropriate status code"""
        order = [order for order in ORDERS_DATA if order["id"] == order_id]
        json_data = request.get_json(force=True, silent=True)

        if not order:
            return PutRespose(order_id).put_order_with_invalid_id_response()
        if not json_data:
            return PutRespose(order_id).\
                put_order_with_empty_entries_response()
        if not OrderItemsValodator(json_data["status"]).is_string_validator():
            return PutRespose(order_id).\
                put_order_with_invalid_status_response()
        if not json_data["status"] in [key for key in STATUS]:
            return PutRespose(order_id).\
                put_order_with_undefined_status_response()
        order[0]["status"] = STATUS[json_data["status"]]
        return PutRespose(order_id).\
            put_order_with_valid_status_response()

    def delete(self, order_id):
        """Delete specific order to return 200 or 404"""
        order = [order for order in ORDERS_DATA if order['id'] == order_id]
        if order:
            ORDERS_DATA.remove(order[0])
            return DeleteResponse(order_id).\
                delete_order_with_valid_id_response()
        return DeleteResponse(order_id).\
            delete_order_with_invalid_id_response()

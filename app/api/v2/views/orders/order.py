"""Module that creates orders endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from ...auth.user_auth import UserAuth

# Local imports
from ...utils.validators import input_validators
from ...responses.orders.order_responses import OrderResponses
from ...models.orders.order import Order
from ...models.users.user import User
from ...auth.user_auth import UserAuth
from ...models.orders.status import Status
from ...responses.orders.status_responses import StatusResponse

parser = reqparse.RequestParser()
parser.add_argument("description", required=False,
    help="description keyword not found")
parser.add_argument("address", required=True,
    help="address keyword not found")
parser.add_argument("meal_id", required=True, type=int,
    help="meal_id keyword not found")
parser.add_argument("quantity", required=True, type=int,
    help="quantity keyword not found")

# Admin Access Endiponts

class ClassInitializer:
    def __init__(self):
        self.order_status = Status()
        self.auth = UserAuth()
        self.user = User()
        self.resp = OrderResponses()
        self.order = Order()

class Orders(Resource, ClassInitializer):
    """Class that creates post and get endpoints"""
    def __init__(self):
        ClassInitializer.__init__(self)

    @jwt_required
    def get(self):
        """Method that  gets resources"""
        if get_jwt_identity():
            user_id = int(get_jwt_identity()) 
            role_name = self.user.get_role_name_by_user_id(user_id)
            if  role_name[0] == "admin":
                orders = self.order.get_all_orders()
                if orders:
                    return self.resp.exists_user_orders_response(orders)
                return self.resp.user_orders_does_not_exists_response()
            return self.resp.forbidden_user_access_response
        return self.resp.unlogged_in_user_response()


class OrderActivity(Resource, ClassInitializer):
    def __init__(self):
        ClassInitializer.__init__(self)

    @jwt_required
    def get(self, order_id):
        """Method that  gets resources"""
        if get_jwt_identity():
            user_id = int(get_jwt_identity())
            role_name = self.user.get_role_name_by_user_id(user_id)
            if  role_name[0] == "admin":
                users_order = self.order.get_order_by_id(order_id)
                if users_order:
                    status = self.order_status.get_order_status_by_id(order[6])
                    return self.resp.exists_user_order_response(users_order, status)
                return self.resp.user_order_does_not_exists_response(order_id)
            return self.resp.forbidden_user_access_response()
        return self.resp.unlogged_in_user_response()

    @jwt_required
    def put(self, order_id):
        """Method that update a particular resource"""
        parser = reqparse.RequestParser()
        parser.add_argument("status", required=True, type=int,
            help="Key word status not found")
        data_parsed = parser.parse_args()
        status = data_parsed["status"]
        if get_jwt_identity():
            user_id = int(get_jwt_identity())
            role_name = self.user.get_role_name_by_user_id(user_id)
            if  role_name[0] == "admin":
                is_valid= input_validators(status=status)
                available_status = self.order.get_all_status()
                if is_valid[0]:
                    if self.order.update_order_status(order_id, status):
                        return self.resp.order_updated_response(order_id)
                    return self.resp.request_order_does_not_exists_response(order_id)
                return self.resp.create_order_with_invalid_contents_response(is_valid[1])
            return self.resp.forbidden_user_access_response()
        return self.resp.unlogged_in_user_response()


class OrderStatus(Resource, ClassInitializer):
    def __init__(self):
        ClassInitializer.__init__(self)

    def get(self, st_code):
        """Method that get a particular resource"""
        status = self.order_status.get_order_status_by_id(st_code)
        if status:
            order = Order().get_order_by_status(status[0])
            if order:
                return {
                    "Id": order[0], "Name": order[1] + " " + order[2],
                    "Meal": order[3], "Quantity": order[4],
                    "Description": order[5], 
                    "Status": status[1], "Delivery Address": order[7],
                    "Created Date": str(order[8]),
                    "Delivery Time": str(order[9])}, 200
            return StatusResponse(st_code, status[1]).order_with_status_code_does_not_exist_response()
        return StatusResponse(st_code).status_does_not_exist_response()


# Normal User Access Endiponts


class UserOrders(Resource):
    """Class that creates post and get endpoints"""
    def __init__(self):
        self.order_status = Status()
        self.auth = UserAuth()
        self.user = User()
        self.resp = OrderResponses()
        self.order = Order()


    @jwt_required
    def get(self):
        """Method that  gets resources"""
        if get_jwt_identity():
            user_id = int(get_jwt_identity())
            user_orders = self.order.get_all_user_orders(user_id)
            if user_orders:
                return self.resp.exists_user_orders_response(user_orders)
            return self.resp.user_orders_does_not_exists_response()
        return self.resp.unlogged_in_user_response()

    @jwt_required
    def post(self):
        """Method that creates resources"""    
        data_parsed = parser.parse_args()
        description = data_parsed["description"].lower()
        address = data_parsed["address"].lower()
        meal_id = data_parsed["meal"]
        quantity = data_parsed["quantity"]
        if get_jwt_identity():
            user_id = int(get_jwt_identity())
            is_valid = input_validators(
                description=description, address=address,
                meal=meal, quantity=quantity)
            if is_valid[0]:
                order_id = self.order.create_order(user_id, address, meal_id, quantity)
                return self.resp.order_created_response(order_id)
            return self.resp.create_order_with_invalid_contents_response(is_valid[1])
        return self.resp.unlogged_in_user_response()


class UserOrderActivity(Resource, ClassInitializer):
    def __init__(self):
        ClassInitializer.__init__(self)

    @jwt_required
    def get(self, order_id):
        """Method that get a particular resource"""
        if get_jwt_identity():
            user_id = int(get_jwt_identity())
            user_order = self.order.get_user_order_by_id(order_id, user_id)
            if user_order:
                status = self.order_status.get_order_status_by_id(order[6])
                return self.resp.exists_user_order_response(user_order, status)
            return self.resp.user_order_does_not_exists_response(order_id)
        return self.resp.unlogged_in_user_response()

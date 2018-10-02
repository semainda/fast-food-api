"""Module that creates orders endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse

# Local imports
from ...utils.validators import input_validators
from ...responses import responses
from ...models.orders.order import Order


class Orders(Resource):
    """Class that creates post and get endpoints"""
    def post(self):
        """Method that creates resources"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "description",
            required=False,
            help="description keyword not found")
        parser.add_argument(
            "user",
            required=True,
            type=int,
            help="user keyword not found")
        parser.add_argument(
            "address",
            required=True,
            help="address keyword not found")
        parser.add_argument(
            "meal",
            required=True,
            type=int,
            help="meal keyword not found")
        parser.add_argument(
            "quantity",
            required=True,
            type=int,
            help="quantity keyword not found")
    
        data_parsed = parser.parse_args()

        description = data_parsed["description"].lower()
        user = data_parsed["user"]
        address = data_parsed["address"].lower()
        meal = data_parsed["meal"]
        quantity = data_parsed["quantity"]

        is_valid = input_validators(
            description=description,
            user=user, address=address,
            meal=meal, quantity=quantity)
        if is_valid:
            Order().create_order(user, address, meal, quantity)
            return responses.resource_success_response()
        return responses.resource_with_invalid_entries_response()

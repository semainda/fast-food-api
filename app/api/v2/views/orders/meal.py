"""Module that creates meal endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse

# Local imports
from ...utils.validators import input_validators
from ...responses import responses
from ...models.orders.meal import Meal
from ...models.orders.category import Category


class Meals(Resource):
    """Class that creates post and get endpoints"""
    def get(self):
        """Method that  gets resources"""
        meals = Meal().get_all_meals()
        if meals:
            return meals, 200
        return responses.resource_does_not_exist_response()

    def post(self):
        """Method that creates meal resources"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "meal",
            required=True,
            help="meal keyword not found")
        parser.add_argument(
            "category",
            required=True,
            help="category keyword not found")
        parser.add_argument(
            "description",
            required=True,
            help="description keyword not found")
        parser.add_argument(
            "price",
            required=True,
            type=int,
            help="price keyword not found")

        data_parsed = parser.parse_args()
        meal = data_parsed["meal"].lower()
        category = data_parsed["category"].lower()
        description = data_parsed["description"].lower()
        price = data_parsed["price"]

        is_valid = input_validators(
            meal=meal, category=category,
            description=description, price=price)
        cat_id = Category().get_category_by_name(category)
        if is_valid:
            if cat_id:
                if not Meal().get_meal_by_name(meal):
                    Meal().create_meal(meal, cat_id, description, price)
                    return responses.resource_success_response()
                return responses.resource_already_exist_response()
            return responses.resource_does_not_exist_response()
        return responses.resource_with_invalid_entries_response()


class MealsActivity(Resource):
    """Class that creates endpoints for particular resource"""
    def get(self, meal_id):
        """Method that get a particular resource"""
        meal = Meal().get_meal_by_id(meal_id)
        if meal:
            return {"Name": meal[0].upper(),
                    "Description": meal[1].upper(),
                    "Price": "TZS "+str(meal[2]),
                    "Category": meal[3].upper()}, 200
        return responses.resource_does_not_exist_response()
    
    def put(self, meal_id):
        """Method that update a particular resource"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "meal",
            required=True,
            help="meal keyword not found")
        parser.add_argument(
            "category",
            required=True,
            help="category keyword not found")
        parser.add_argument(
            "description",
            required=True,
            help="description keyword not found")
        parser.add_argument(
            "price",
            required=True,
            type=int,
            help="price keyword not found")

        data_parsed = parser.parse_args()
        meal = data_parsed["meal"].lower()
        category = data_parsed["category"].lower()
        description = data_parsed["description"].lower()
        price = data_parsed["price"]

        is_valid = input_validators(
            meal=meal, category=category,
            description=description, price=price)
        if is_valid:
            cat_id = Category().get_category_by_name(category)
            if cat_id:
                if Meal().get_meal_by_id(meal_id):
                    Meal().update_all_meal_entries(meal, cat_id, description, price, meal_id)
                    return responses.resource_success_response()
                return responses.resource_does_not_exist_response()
            return responses.resource_does_not_exist_response()
        return responses.resource_with_invalid_entries_response()

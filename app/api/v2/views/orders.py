"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask_restful import Resource, reqparse

# Local imports
from ..utils import post_validators
from ..responses import orders_responses

# models imports
from ..models.categories import CategoriesModel
from ..models.meals import MealsModel

# Categories

categories = CategoriesModel().get_all_categories()


class Categories(Resource):
    """Class for post and get categories"""
    def get(self):
        """Method to query the database and return all categories"""
        if categories:
            return orders_responses.return_resources_response(
                categories, "Categories")
        return orders_responses.resource_does_not_exist_response()

    def post(self):
        """Method querying the database to create category"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "category", required=True,
            help="Menu category can't be empty")
        data_parsed = parser.parse_args()
        category = data_parsed["category"]
        output = post_validators.order_str_data_validator(category=category)
        if output:
            if categories:
                cat_names = [cat_name[1] for cat_name in categories]
                if category in cat_names:
                    return orders_responses.resource_already_exist_response()
                CategoriesModel().post_category(category)
                return orders_responses.resource_success_response()
            CategoriesModel().post_category(category)
            return orders_responses.resource_success_response()
        return orders_responses.resource_with_invalid_entries_response()


class CategoriesActivity(Resource):
    def get(self, cat_id):
        """Method quering the database and return one category"""
        cat_ids = [cat_id[0] for cat_id in categories]
        if cat_id in cat_ids:
            return orders_responses.return_single_resource_response(
                CategoriesModel().get_category(cat_id),
                "Category")
        return orders_responses.resource_does_not_exist_response()

    def put(self, cat_id):
        """Method quering the database to update one category"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "category", required=True,
            help="Menu category can't be empty")
        data_parsed = parser.parse_args()
        category = data_parsed["category"]
        output = post_validators.order_str_data_validator(category=category)
        if output:
            cat_ids = [cat_id[0] for cat_id in categories]
            if cat_id in cat_ids:
                CategoriesModel().put_category(category, cat_id)
                return orders_responses.resource_success_response()
            return orders_responses.resource_does_not_exist_response()
        return orders_responses.resource_with_invalid_entries_response()

    def delete(self, cat_id):
        """Method quering the database to delete one category"""
        cat_ids = [cat_id[0] for cat_id in categories]
        if cat_id in cat_ids:
            CategoriesModel().delete_category(cat_id)
            return orders_responses.resource_success_response()
        return orders_responses.resource_does_not_exist_response()


# Meals

meals = MealsModel().get_all_meals()


class Meals(Resource):
    """Class for post and get categories"""
  
    def post(self):
        """Method querying the database to create menu"""  meal_name, cat_id, description, price
        parser = reqparse.RequestParser()
        parser.add_argument(
            "meal", required=True,
            help="Meal can't be empty")
        parser.add_argument(
            "cat_id", required=True,
            help="Category can't be empty")
        parser.add_argument(
            "description", required=True,
            help="Description can't be empty")
        parser.add_argument(
            "price", required=True,
            help="Price can't be empty")
        data_parsed = parser.parse_args()
        meal = data_parsed["meal"]
        category = data_parsed["cat_id"]
        description = data_parsed["description"]
        price = data_parsed["price"]

        valid_str = post_validators.order_str_data_validator(meal=meal, description=description, price=price)
        valid_int = post_validators.order_int_data_validator(category=category, price=price)

        if valid_str:
            if valid_int:
                meal_cat = CategoriesModel().get_category(category)
                if meal_cat:
                    if meals:
                        meal_names = [meal_name[1] for meal_name in meals]
                        if meal in meals_names:
                            return orders_responses.resource_already_exist_response()
                        MealsModel().post_meal(meal)
                        return orders_responses.resource_success_response()
                    MealsModel().post_meal(meal)
                return orders_responses.resource_does_not_exist_response()
            return orders_responses.resource_with_invalid_entries_response()
        return orders_responses.resource_with_invalid_entries_response()

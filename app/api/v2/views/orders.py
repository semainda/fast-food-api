"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask_restful import Resource, reqparse

# Local imports
from ..utils import post_validators
from ..responses import orders_responses

# models imports
from ..models.categories import CategoriesModel

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

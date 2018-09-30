"""Module that creates categories endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse

# Local imports
from ...utils.validators import input_validators
from ...responses import responses
from ...models.orders.category import Category


class Categories(Resource):
    """Class that creates post and get endpoints"""
    def get(self):
        """Method that  gets resources"""
        categories = Category().get_all_categories()
        if categories:
            return responses.return_resources_response(categories)
        return responses.resource_does_not_exist_response()

    def post(self):
        """Method that creates resources"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "category",
            required=True,
            help="category keyword not found")
        data_parsed = parser.parse_args()
        category = data_parsed["category"]

        is_valid = input_validators(category=category)
        if is_valid:
            if not Category().get_category_by_name(category):
                Category().create_category(category)
                return responses.resource_success_response()
            return responses.resource_already_exist_response()
        return responses.resource_with_invalid_entries_response()


class CategoriesActivity(Resource):
    """Class that creates endpoints for particular resource"""
    def get(self, cat_id):
        """Method that get a particular resource"""
        category = Category().get_category_by_id(cat_id)
        if category:
            return responses.return_resources_response(category)
        return responses.resource_does_not_exist_response()

    def put(self, cat_id):
        """Method that update a particular resource"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "category",
            required=True,
            help="category keyword not found")
        data_parsed = parser.parse_args()
        category = data_parsed["category"]
        is_valid= input_validators(category=category)
        if is_valid:
            if Category().update_category(category, cat_id):
                return responses.resource_success_response()
            return responses.resource_does_not_exist_response()
        return responses.resource_with_invalid_entries_response()

    def delete(self, cat_id):
        """Method that delete a particular resource"""
        if Category().delete_category(cat_id):
            return responses.resource_success_response()
        return responses.resource_does_not_exist_response()

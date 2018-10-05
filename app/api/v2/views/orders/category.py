"""Module that creates categories endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse

# Local imports
from ...utils.validators import input_validators
from ...responses import responses
from ...responses.orders.category_responses import CategoryResponses
from ...models.orders.category import Category


class Categories(Resource):
    """Class that creates post and get endpoints"""
    def __init__(self):
        self.resp = CategoryResponses()

    def get(self):
        """Method that  gets resources"""
        categories = Category().get_all_categories()
        if categories:
            return self.resp.request_exists_categories_response(categories)
        return self.resp.request_categories_does_not_exists_response()

    def post(self):
        """Method that creates resources"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "category",
            required=True, help="Key not found")
        data_parsed = parser.parse_args()
        category = data_parsed["category"].lower()

        is_valid = input_validators(category=category)
        if is_valid[0]:
            if not Category().get_category_by_name(category):
                Category().create_category(category)
                return self.resp.category_created_response(category)
            return self.resp.category_already_exist_response(category)
        return self.resp.create_category_with_invalid_contents_response(is_valid[1])


class CategoriesActivity(Resource):
    """Class that creates endpoints for particular resource"""
    def __init__(self):
        self.resp = CategoryResponses()

    def get(self, cat_id):
        """Method that get a particular resource"""
        category = Category().get_category_by_id(cat_id)
        if category:
            return self.resp.request_exists_category_response(category)
        return self.resp.request_category_does_not_exists_response(cat_id)

    def put(self, cat_id):
        """Method that update a particular resource"""
        parser = reqparse.RequestParser()
        parser.add_argument(
            "category",
            required=True)
        data_parsed = parser.parse_args()
        category = data_parsed["category"]
        is_valid= input_validators(category=category)
        if is_valid[0]:
            if Category().update_category(category, cat_id):
                return self.resp.category_updated_response(category)
            return self.resp.request_categories_does_not_exists_response()
        return self.resp.create_category_with_invalid_contents_response(is_valid[1])

    def delete(self, cat_id):
        """Method that delete a particular resource"""
        deleted_category = Category().delete_category(cat_id)
        if deleted_category:
            return self.resp.category_deleted_response(deleted_category)
        return self.resp.request_categories_does_not_exists_response()

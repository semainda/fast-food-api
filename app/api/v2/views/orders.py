"""This module contains all api endpoints"""
# Thirdparty imports
from datetime import datetime
from flask_restful import Resource, reqparse

# Local imports
from ..utils import post_validators
from ..responses import orders_responses

## models imports
from ..models.categories import CategoriesModel

categories = CategoriesModel().get_all_categories()

class Categories(Resource):
  
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("category", required=True, help="Menu category can't be empty")
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
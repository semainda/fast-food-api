"""Module that creates meal endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

# Local imports
from ...utils.validators import input_validators
from ...responses import responses
from ...models.orders.meal import Meal
from ...models.orders.category import Category
from ...models.users.user import User
from ...responses.orders.meal_responses import MealResponses

parser = reqparse.RequestParser()
parser.add_argument("meal", required=True,
    help="keyword meal not found")
parser.add_argument("category", required=True,
    help="keyword category not found")
parser.add_argument("description", required=True,
    help="keyword description not found")
parser.add_argument("price", required=True, type=int,
    help="keyword price not found")

class Meals(Resource):
    """Class that creates post and get endpoints"""
    def __init__(self):
        self.user = User()
        self.resp = MealResponses()

    def get(self):
        """Method that  gets resources"""
        meals = Meal().get_all_meals()
        if meals:
            return meals, 200
        return responses.resource_does_not_exist_response()

    @jwt_required
    def post(self):
        """Method that creates meal resources"""
        data_parsed = parser.parse_args()
        meal = data_parsed["meal"].lower()
        category = data_parsed["category"].lower()
        description = data_parsed["description"].lower()
        price = data_parsed["price"]

        if get_jwt_identity():
            user_id = int(get_jwt_identity()) 
            role_name = self.user.get_role_name_by_user_id(user_id)
            if  role_name[0] == "admin":
                is_valid = input_validators(
                    meal=meal, category=category,
                    description=description, price=price)
                cat_id = Category().get_category_by_name(category)
                if is_valid[0]:
                    if cat_id:
                        if not Meal().get_meal_by_name(meal):
                            Meal().create_meal(meal, cat_id, description, price)
                            return self.resp.meal_created_response(meal)
                        return self.resp.meal_already_exist_response(meal)
                    return self.resp.meal_does_not_exists_response(category)
                return self.resp.meal_with_invalid_contents_response(is_valid[1])
            return self.resp.uathorization_response()
        return self.resp.login_responses()


class MealsActivity(Resource):
    """Class that creates endpoints for particular resource"""
    def __init__(self):
        self.user = User()
        self.resp = MealResponses()

    def get(self, meal_id):
        """Method that get a particular resource"""
        meal = Meal().get_meal_by_id(meal_id)
        if meal:
            return self.resp.exists_meal_response(meal)
        return self.resp.meal_does_not_exists_response(meal)
    
    def put(self, meal_id):
        """Method that update a particular resource"""
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
                    Meal().update_all_meal_entries(meal, cat_id,
                    description, price, meal_id)
                    return self.resp.meal_updated_response(meal)
                return self.resp.meal_does_not_exists_response(meal)
            return self.resp.meal_does_not_exists_response(category)
        return self.resp.meal_with_invalid_contents_response(is_valid[1])

    def delete(self, meal_id):
        """Method that delet particular resource"""
        if Meal().delete_meal(meal_id):
            return self.resp.meal_deleted_response(meal_id)
        return self.resp.meal_already_exist_response(meal_id)

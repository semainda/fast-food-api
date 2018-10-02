"""Module that creates users endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse

# Local imports
from ...utils.validators import input_validators
from ...responses import responses
from ...models.users.user import User
from .roles import user_roles


class Users(Resource):
    """Class that creates post and get endpoints"""
    def get(self):
        """Method that  gets resources"""
        users = User().get_all_users()
        if users:
            return users, 200
        return responses.resource_does_not_exist_response()

    def post(self):
        """Method that creates users"""
        parser = reqparse.RequestParser()
        parser.add_argument("first_name",
                            required=True,
                            help="first_name keyword not found")
        parser.add_argument("last_name",
                            required=True,
                            help="last_name keyword not found")
        parser.add_argument("email",
                            required=True,
                            help="email keyword not found")
        parser.add_argument("user_name",
                            required=True,
                            help="user_name keyword not found")
        parser.add_argument("password",
                            required=True,
                            help="password keyword not found")

        data_parsed = parser.parse_args()
        first_name = data_parsed["first_name"].lower()
        last_name = data_parsed["last_name"].lower()
        email = data_parsed["email"]
        user_name = data_parsed["user_name"]
        password = data_parsed["password"]

        is_valid = input_validators(
            first_name=first_name,
            last_name=last_name)
        if is_valid:
            if not User().get_user_by_user_name_email(user_name, email):
                User().create_user(
                    first_name, last_name, email, user_name, password)
                return responses.resource_success_response()
            return responses.resource_already_exist_response()
        return responses.resource_with_invalid_entries_response()


class UsersActivity(Resource):
    """Class that contains users specific endpoints"""
    def get(self, user_id):
        """Method that get a particular user"""
        user = User().get_user_by_user_id(user_id)
        if user:
            return {
                "Name": user[1] + " " + user[2], "Email": user[3],
                "Username": user[4], "Role": user[5],
                "Created Date": str(user[8])}, 200
        return responses.resource_does_not_exist_response()
    
    def put(self, user_id):
        """Method that update a particular user details"""
        parser = reqparse.RequestParser()
        parser.add_argument("password",
                            required=True,
                            help="password keyword not found")
        parser.add_argument("email",
                            required=True,
                            help="email keyword not found")
        parser.add_argument("role",
                            required=True,
                            help="role keyword not found")

        data_parsed = parser.parse_args()
        email = data_parsed["email"]
        password = data_parsed["password"]
        role = data_parsed["role"]
        if role in user_roles:
            if User().update_user(email, password, role, user_id):
                return responses.resource_success_response()
            return responses.resource_does_not_exist_response()
        return responses.resource_does_not_exist_response()
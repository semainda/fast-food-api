"""Module that creates users endpoints"""

# Thirdparty imports
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from ...auth.user_auth import UserAuth

# Local imports
from ...utils.validators import input_validators
from ...responses.users.user_responses import UserResponses
from ...models.users.user import User

parser = reqparse.RequestParser()
parser.add_argument("first_name", required=True,
    help="Key word 'first_name' is not found")
parser.add_argument("last_name", required=True,
    help="Key word 'last_name' is not found")
parser.add_argument("email", required=True,
    help="Key word 'email' is not found")
parser.add_argument("user_name", required=True, 
    help="Key word 'user_name' is not found")
parser.add_argument("password", required=True, 
    help="Key word 'password' is not found")


class SignUp(Resource):
    """Class that creates post and get endpoints"""
    def __init__(self):
        self.resp = UserResponses()
        self.auth = UserAuth()
        self.user = User()

    def post(self):
        """Method that signups users"""
        data_parsed = parser.parse_args()
        first_name = data_parsed["first_name"].lower()
        last_name = data_parsed["last_name"].lower()
        email = data_parsed["email"]
        user_name = data_parsed["user_name"]
        password = self.auth.generate_hash_password(data_parsed["password"])

        is_valid = input_validators(first_name=first_name, last_name=last_name)
        if is_valid[0]:
            current_user = self.user.get_user_by_user_name_email(
                user_name, email)
            if not current_user:
                new_user = self.user.create_user(first_name,
                    last_name, email, user_name, password)
                return self.resp.user_created_response(user_name)
            return self.resp.user_already_exist_response(user_name)
        return self.resp.sign_up__with_invalid_details_response(is_valid[1])


class Users(Resource): # return list of system users
    """Class that creates post and get endpoints"""
    def __init__(self):
        self.resp = UserResponses()
        self.auth = UserAuth()
        self.user = User()

    @jwt_required
    def get(self):
        """Method that  gets resources"""
        if get_jwt_identity():
            user_id = int(get_jwt_identity())
            role_name = self.user.get_role_name_by_user_id(user_id)
            if  role_name[0] == "admin":       
                users = self.user.get_all_users()
                if users:
                    return self.resp.exists_users_response(users)
                return self.resp.users_does_not_exists_response()
            return self.resp.forbidden_user_access_response()
        return self.resp.unauthorized_user_access_responses()


class UsersActivity(Resource):
    """Class that contains users specific endpoints"""
    def __init__(self):
        self.user = User()
        self.resp = UserResponses()

    @jwt_required
    def get(self, user_id):
        """Method that get a particular user"""
        role_id = self.user.get_role_id_by_user_id(user_id)
        if role_id:
            if  get_jwt_identity() == role_id[0]:
                user = self.user.get_user_by_user_id(user_id)
                if user:
                    return self.resp.exist_user_response(user)
                return self.resp.user_does_not_exists_response(user_id)
            return role_id
        return self.resp.forbidden_user_access_response()
        # self.resp.unauthorized_user_access_responses()


    @jwt_required
    def put(self, user_id):
        """Method that update a particular user details"""
        # Any logged in user can update his or her details
        if get_jwt_identity():
            data_parsed = parser.parse_args()
            email = data_parsed["email"]
            password = data_parsed["password"]
            user_id = self.user.update_user(email, password, user_id)
            if user_id:
                return self.resp.user_details_update_response(user_id)
            return self.resp.user_does_not_exists_response(user_id)
        return self.resp.unauthorized_user_access_responses()

    @jwt_required
    def delete(self, user_id):
        """Method that delete a particular resource"""
        role_name = self.user.get_user_role_name(get_jwt_identity())
        if  role_name== "admin":
            user_id = self.user.delete_user(user_id)
            if user_id:
                return self.resp.user_deleted_response(user_id)
            return responses.resource_does_not_exist_response()
        return self.resp.forbidden_user_access_response()

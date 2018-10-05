"""Module that handle user logins"""
# thirdparty imports
from flask_restful import Resource, reqparse
# local imports
from ...auth.user_auth import UserAuth
from ...models.users.user import User
from ...responses.users.user_responses import UserResponses

parser = reqparse.RequestParser()
parser.add_argument("user_name", required=True,
    help="Key user_name not found")
parser.add_argument("password", required=True,
    help="Key password not found")


class Login(Resource):
    """Class that perfom login checks"""
    def __init__(self):
        self.auth = UserAuth()
        self.resp = UserResponses()
        self.user = User()

    def post(self):
        """Method that create user login"""
        data_parsed = parser.parse_args()
        credentals = self.user.get_user_password_and_id(data_parsed["user_name"])
        if credentals:  
            if self.auth.verify_hashed_password(data_parsed["password"], credentals[1]):
                access_token = self.auth.return_access_token(credentals[0])
                return self.resp.valid_user_login_response(data_parsed["user_name"], access_token)
        return self.resp.invalid_user_login_response()
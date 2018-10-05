"""Module that creates categories endpoints"""

# Thirdparty imports
import json
from flask_restful import Resource, reqparse

# Local imports
from ...utils.validators import input_validators
from ...responses import responses
from ...responses.users.role_responses import RoleResponses
from ...models.users.role import Role

parser = reqparse.RequestParser()
parser.add_argument("role_name", required=True, type=str, help="Key role_name not found")


class Roles(Resource):
    """Class that creates post and get endpoints"""
    def __init__(self):
        self.resp = RoleResponses()
        self.role = Role()

    def get(self):
        """Method that  gets roles"""
        roles = self.role.get_all_roles()
        if roles:
            return self.resp.request_exists_roles_response(roles)
        return self.resp.request_roles_does_not_exists_response()

    def post(self):
        """Method that creates role"""
        data_parsed = parser.parse_args()
        role_name = data_parsed["role_name"].lower()

        is_valid = input_validators(role_name=role_name)
        if is_valid[0]:
            role = self.role.get_role_by_name(role_name)
            if not role:
                self.role.create_role(role_name)
                return self.resp.role_created_response(role_name)
            return self.resp.role_already_exist_response(role_name)
        return self.resp.create_category_with_invalid_contents_response(is_valid[1])


class RolesActivity(Resource):
    """Class that creates endpoints for particular resource"""
    def __init__(self):
        self.resp = RoleResponses()
        self.role = Role()

    def get(self, role_id):
        """Method that get a particular resource"""
        role = self.role.get_role_by_id(role_id)
        if role:
            return self.resp.request_exists_role_response(role)
        return self.resp.request_role_does_not_exists_response(role_id)

    def put(self, role_id,):
        """Method that update a particular role"""
        data_parsed = parser.parse_args()
        role_name = data_parsed["role_name"].lower()
        is_valid = input_validators(role_name=role_name)
        if is_valid[0]:
            role_name = self.role.update_role(role_name, role_id)
            if role_name:
                return self.resp.role_updated_response(role_name[0])
            return self.resp.request_role_does_not_exists_response(role_id)
        return self.resp.update_role_with_invalid_contents_response(is_valid[1])

    def delete(self, role_id):
        """Method that delete a particular resource"""
        deleted_role = self.role.deleted_role(role_id)
        if deleted_role:
            return self.resp.role_deleted_response(deleted_role)
        return self.resp.request_role_does_not_exists_response(role_id)


class UserRoles(Resource):
    """Class that creates post and get endpoints"""
    def __init__(self):
        self.resp = RoleResponses()
        self.role = Role()

    def get(self):
        """Method that  gets roles"""
        roles = self.role.get_user_roles()
        if roles:
            return self.resp.request_exists_roles_response(roles)
        return self.resp.request_roles_does_not_exists_response()
    

class UserRolesActivity(Resource):
    def __init__(self):
        self.resp = RoleResponses()
        self.role = Role()

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("role_id", required=True, type=int, help="Key role_id not found")
        data_parsed = parser.parse_args()
        role_id = data_parsed["role_id"]
        is_valid = input_validators(role_id=role_id)
        if is_valid[0]:
            user_role = self.role.update_user_roles(role_id, user_id)
            if user_role:
                return self.resp.role_updated_response(user_role[0])
            return self.resp.request_role_does_not_exists_response(role_id)
        return self.resp.update_role_with_invalid_contents_response(is_valid[1])
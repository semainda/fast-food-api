"""Module that holds meal role responses"""


class RoleResponses:
    """Class that hold all role responses"""

    def request_roles_does_not_exists_response(self):
        """Method that returns roles not found"""
        return {"Message": "Roles does not exists"}, 404
    
    def request_role_does_not_exists_response(self, role_id):
        """Method that returns roles not found"""
        return {"Message": "Role with id '{}' does not exists".format(role)}, 404
    
    def request_exists_roles_response(self, roles):
        """Method that returns categories not found"""
        return {"Roles": roles}, 200

    def request_exists_role_response(self, role):
        """Method that returns categories not found"""
        return {"Role": role[0].upper()}, 200

    def role_already_exist_response(self, role):
        """Method for exist response """
        return {
            "Message": "The role name '{}' already exists"\
            .format(role)}, 409

    def update_role_with_invalid_contents_response(self, role_name):
        """Method for post empty order response"""
        return {
            "Message": "Role name '{}' is invalid for it to be updated"}, 209

    def create_role_with_invalid_contents_response(self, role_name):
        """Method for invalid responses"""
        return {
            "Message": "Role name '{}' is invalid for it to be created"\
            .format(role_name)}, 400

    def role_created_response(self, role):
        """Method for created response"""
        return {
            "Message": "Role '{}' created successful"\
            .format(role)}, 201

    def role_updated_response(self, role):
        """Method for updated response"""
        return {
            "Message": "Role '{}' updated successful"\
            .format(role)}, 201
    
    def role_deleted_response(self, deleted_role):
        """Method for deleted role response"""
        return {
            "Message": "Role '{}' deleted successful"\
            .format(deleted_role)}, 200

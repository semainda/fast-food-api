"""Module that holds user responses"""


class UserResponses:
    """Class that hold all users responses"""

    def invalid_user_login_response(self):
        """Method that returns incorrect login"""
        return {"Message": "Incorrect username or password"}, 401
    
    def valid_user_login_response(self, user_role, access_token):
        """Method that returns valid login response"""
        return{'message': 'Holaa! You Logged in as {}'.format(user_role),
                'access_token': access_token}, 201
    
    def exists_users_response(self, users):
        """Method that returns users not found"""
        return {"Users": users}, 200
    
    def users_does_not_exists_response(self):
        """Method that returns users not found"""
        return {"Message": "Users does not exists"}, 404
    
    def user_created_response(self, user):
        """Method for create response"""
        return {
            "Message": "User with username '{}' created successful"\
            .format(user)}, 201
    
    def user_already_exist_response(self, user_name):
        """Method for exist response """
        return {
            "Message": "User with username '{}' already exists"\
            .format(user_name.upper())}, 409
    
    def sign_up__with_invalid_details_response(self, detail):
        """Method for invalid responses"""
        return {
            "Message": "'{}' is invalid for it to be created"\
            .format(detail)}, 400
    
    def user_does_not_exists_response(self, user_id):
        """Method that returns user not found"""
        return {"Message": "User with id '{}' does not exists"\
        .format(user_id)}, 404
    
    def exist_user_response(self, user):
        """Method that returns users not found"""
        return {"Name": user[1] + " " + user[2], "Email": user[3],
                "Username": user[4],"Created Date": str(user[6])}, 200
    
    def user_details_update_response(self, user_id):
        """Method for updated user details response"""
        return {
            "Message": "User details with id '{}' updated successful"\
            .format(user_id)}, 200
    
    def user_deleted_response(self, user_id):
        """Method for deleted user response"""
        return {
            "Message": "User details with id '{}' deleted successful"\
            .format(user_id)}, 200
    
    def user_role_does_not_exists_response(self, role):
        """Method that returns users not found"""
        return {"Message": "User role '{}' does not exists"}, 404

    def forbidden_user_access_response(self):
        """Method for returning unauthorized response"""
        return {
            "Message": "Your access is denied to this resource"
        }, 403
    
    def unauthorized_user_access_responses(self):
        """Method for returning unauthorized response"""
        return {
            "Message": "You are not logged in to access this resource"
        }, 401
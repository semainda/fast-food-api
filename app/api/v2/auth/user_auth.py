# thirdparty imports
from flask_jwt_extended import create_access_token,\
jwt_required, get_jwt_identity

from passlib.hash import pbkdf2_sha256 as hash07936

class UserAuth:

    def generate_hash_password(self, password):
        """ Method that generate hashed password"""
        return hash07936.hash(password)
    
    def verify_hashed_password(self, loggedin_password, current_password):
        """
            Method that verify the hashed agains loggedin password,
            returns true if match found otherwise false
        """
        return hash07936.verify(loggedin_password, current_password)
    
    def return_access_token(self, token_identity):
        """Method that creates and returns user access token"""
        return create_access_token(identity=token_identity)


    
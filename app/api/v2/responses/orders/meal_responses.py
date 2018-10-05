"""Module that holds meal meal responses"""


class MealResponses:
    """Class that hold all meal responses"""

    def meal_created_response(self, meal):
        """Method for created response"""
        return {
            "Message": "Meal '{}' created successful"\
            .format(meal)}, 201
    
    def meal_already_exist_response(self, meal):
        """Method for exist response """
        return {
            "Message": "Meal '{}' already exists"\
            .format(meal)}, 409

    def meal_does_not_exists_response(self, cat_name):
        """Method that returns categories not found"""
        return {
            "Message": "Meal '{}' does not exists"\
            .format(cat_name)}, 404
    
    def meal_with_invalid_contents_response(self, name):
        """Method for invalid responses"""
        return {
            "Message": "Meal '{}' is invalid for it to be created"\
            .format(name)}, 400
    
    def uathorization_response(self):
        return {"Message": "Your access is denied to this resource"}, 403

    def login_responses(self):
        return {"Message": "Sorry! Your not logged in"}, 401

    def meal_updated_response(self, meal):
        """Method for updated response"""
        return {
            "Message": "Meal with id '{}' updated successful"\
            .format(meal)}, 201

    def meal_deleted_response(self, meal):
        """Method for deleted category response"""
        return {
            "Message": "Meal with'{}' deleted successful"\
            .format(meal)}, 200

    def exists_meal_response(self, meal):
        """Method that returns"""
        return {"Name": meal[0].upper(),
                "Description": meal[1].upper(),
                "Price": "TZS "+str(meal[2]),
                "Category": meal[3].upper()}, 200

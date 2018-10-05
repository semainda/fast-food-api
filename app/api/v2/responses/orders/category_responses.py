"""Module that holds meal category responses"""


class CategoryResponses:
    """Class that hold all category responses"""

    def request_categories_does_not_exists_response(self):
        """Method that returns categories not found"""
        return {"Message": "Categorie(s) does not exists"}, 404
    
    def request_category_does_not_exists_response(self, cat_id):
        """Method that returns categories not found"""
        return {"Message": "Category with id '{}' does not exists".format(cat_id)}, 404

    def request_exists_categories_response(self, categories):
        """Method that returns categories not found"""
        return {"Categories": categories}, 200

    def request_exists_category_response(self, category):
        """Method that returns categories not found"""
        return {"Category": category[0].upper()}, 200

    def category_already_exist_response(self, category):
        """Method for exist response """
        return {
            "Message": "The category '{}' already exists"\
            .format(category)}, 409

    def create_update_category_with_no_contents_response(self):
        """Method for post empty order response"""
        return {
            "Message": "Create category with no content not allowed"}, 204

    def create_category_with_invalid_contents_response(self, category_name):
        """Method for invalid responses"""
        return {
            "Message": "Category name '{}' is invalid for it to be created"\
            .format(category_name)}, 400

    def category_created_response(self, category):
        """Method for created response"""
        return {
            "Message": "Category '{}' created successful"\
            .format(category)}, 201
    
    def category_updated_response(self, category):
        """Method for updated response"""
        return {
            "Message": "Category '{}' updated successful"\
            .format(category)}, 201
    
    def category_deleted_response(self, category):
        """Method for deleted category response"""
        return {
            "Message": "Category '{}' deleted successful"\
            .format(category)}, 200

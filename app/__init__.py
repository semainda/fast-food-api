"""This module is the backbone of our app as it real creates a flask app"""
# Thirdparty imports
from flask import Flask, Blueprint
from flask_restful import Api

# Local imports
from instance.config import APP_ENV_CONFIG
from .api.v2.views.orders.category import Categories, CategoriesActivity
from .api.v2.views.orders.meal import Meals
from .db_config.db_setups import DatabaseOperations


# create api and blueprint objects
api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

def create_app(config_key):
    """This function is the one that creates flask app
    with given configuration"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_ENV_CONFIG[config_key])
    app.config.from_pyfile('config.py')

    # database table creation
    DatabaseOperations().create_db_tables(app.config["DATABASE_URL"])

    # blueprint registration
    app.register_blueprint(api_blueprint, url_prefix="/api/v2")
    
    return app

# add the api routes
api.add_resource(Categories, "/menu/categories")
api.add_resource(CategoriesActivity, "/menu/categories/<int:cat_id>")
api.add_resource(Meals, "/menu")

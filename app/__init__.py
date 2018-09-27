"""This module is the backbone of our app as it real creates a flask app"""
# Thirdparty imports
from flask import Flask, Blueprint
from flask_restful import Api

# Local imports
from instance.config import APP_CONFIG
from .api.v2.views.orders import Categories


# create api and blueprint objects
api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

def create_app(config_name):
    """This function is the one that creates flask app
    with given configuration"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    #create_dev_db_tables()

    # blueprint registration
    app.register_blueprint(api_blueprint, url_prefix="/api/v2")

    # add the api routes
    # api.add_resource(Orders, "/orders")
    # api.add_resource(OrderActivity, "/orders/<int:order_id>")
    # menu categories endpoints
    api.add_resource(Categories, "/menu/categories")

    return app


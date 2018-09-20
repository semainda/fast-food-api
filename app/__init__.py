"""This module is the backbone of our app as it real creates a flask app"""
# Thirdparty imports
from flask import Flask

# Local imports
from instance.config import APP_CONFIG


def create_app(config_name):
    """This function is the one that creates flask app
    with given configuration"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    return app

"""This module is the backbone of our app as it real creates a flask app"""
# Thirdparty imports
from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Local imports
from instance.config import APP_ENV_CONFIG
from .api.v2.views.orders.category import Categories, CategoriesActivity
from .api.v2.views.orders.meal import Meals, MealsActivity
from .api.v2.views.users.user import Users, UsersActivity, SignUp
from .api.v2.views.orders.order import Orders, OrderActivity,\
OrderStatus, UserOrders, UserOrderActivity
from .api.v2.views.users.login import Login
from .api.v2.views.users.role import Roles, RolesActivity, UserRoles, UserRolesActivity
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
    
    # Add JWT
    JWTManager(app)
    return app

# public endpoints 
api.add_resource(Login, "/auth/login")
api.add_resource(SignUp, "/auth/signup")

# Secured endpoints

# users order api routes
api.add_resource(UserOrders, "/users/orders")
api.add_resource(UserOrderActivity, "/users/orders/<int:order_id>")

# admin order api routes
api.add_resource(Orders, "/orders/")
api.add_resource(OrderActivity, "/orders/<int:order_id>")
api.add_resource(OrderStatus, "/orders/status/<int:status_id>")

# add meals api routes
api.add_resource(Meals, "/menu")
api.add_resource(MealsActivity, "/menu/<int:meal_id>")

# admin categories api routes
api.add_resource(Categories, "/menu/categories")
api.add_resource(CategoriesActivity, "/menu/categories/<int:cat_id>")

# admin role api route
api.add_resource(Roles, "/roles")
api.add_resource(RolesActivity, "/roles/<int:role_id>")

# admin role api route
api.add_resource(UserRoles, "/users/roles")
api.add_resource(UserRolesActivity, "/users/roles/<int:user_id>")
# admin users api routes
api.add_resource(Users, "/users")
api.add_resource(UsersActivity, "/users/<int:user_id>")







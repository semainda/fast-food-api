"""This module is used to run our entire flask application"""
# Thirdparty imports
import os

# Local imports
from app import create_app

# Create enviroment that our app will use in the running process
CONFIG = os.getenv("APP_SETTINGS")

app = create_app(CONFIG)

if __name__ == "__main__":
    app.run()

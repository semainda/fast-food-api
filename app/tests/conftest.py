"""This module contains configurations that will accomodate testing"""
# Thirdparty imports
import os
import pytest
from flask import current_app
# Local imports
from app import create_app
from ..db_config.db_setups import DatabaseOperations
# from app.db_setups import create_db_tables, destroy_db_tables

TEST_CONFIG = os.getenv("ENV_CONFIG")

@pytest.fixture(scope="session")
def test_client():
    """This function is used to initialize setting,
    acquare some resources before tests runs
    and release them when testing is done"""
    # setup

    app = create_app(TEST_CONFIG)
    testing_client = app.test_client()

    # stop the flow and passes control to the tests
    yield testing_client
    # pick up here when tests are done
    #with app.app_context():
        #db = DatabaseOperations()
        #conn = db.destroy_db_tables(app.config["DATABASE_URL"])
        #conn.close()
        


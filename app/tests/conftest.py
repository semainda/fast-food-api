"""This module contains configurations that will accomodate testing"""
# Thirdparty imports
import os
import pytest

# Local imports
from app import create_app

CONFIG = os.getenv('APP_SETTINGS')


@pytest.fixture
def test_client():
    """This function is used to initialize setting,
    acquare some resources before tests runs
    and release them when testing is done"""
    # setup
    app = create_app(CONFIG)
    testing_client = app.test_client()

    # stop the flow and passes control to the tests
    yield testing_client
    # pick up here when tests are done

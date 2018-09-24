"""This module contains configurations that will accomodate testing"""
# Thirdparty imports
import os
import pytest

# Local imports
from app import create_app

TEST_CONFIG = os.getenv('TEST_CONFIG')


@pytest.fixture
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

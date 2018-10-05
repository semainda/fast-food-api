"""This module contains all of our application environment"""
import os

class Config:
    DEBUG = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class DevelopmentConfig(Config):
    """Defining configurations required for development purpose"""
    DEBUG = True
    DATABASE_URL = os.getenv("DEV_DATABASE_URL")
    # "dbname='fastdev_db' user='postgres' host='127.0.0.1' password='semainda'"  development db

class TestingConfig(Config):
    """Defining configurations required for testing purpose"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv("TEST_DATABASE_URL")
    # "dbname='fasttest_db' user='postgres' host='127.0.0.1' password='semainda'"  testing db


class ProductionConfig(Config):
    """Defining configurations required for production purpose"""
    DEBUG = False
    TESTING = False


APP_ENV_CONFIG = {
    "test_env": TestingConfig,
    "dev_env": DevelopmentConfig,
    "pro_env": ProductionConfig
}

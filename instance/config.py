"""This module contains all of our application environment"""
import os

class Config:
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    """Defining configurations required for development purpose"""
    DEBUG = True


class TestingConfig(Config):
    """Defining configurations required for testing purpose"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = os.getenv("TEST_DATABASE_URL")


class ProductionConfig(Config):
    """Defining configurations required for production purpose"""
    DEBUG = False
    TESTING = False


APP_CONFIG = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

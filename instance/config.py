"""This module contains all of our application environment"""


class DevelopmentConfig:
    """Defining configurations required for development purpose"""
    DEBUG = True


class TestingConfig:
    """Defining configurations required for testing purpose"""
    DEBUG = True
    TESTING = True


class ProductionConfig:
    """Defining configurations required for production purpose"""
    DEBUG = False
    TESTING = True


APP_CONFIG = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

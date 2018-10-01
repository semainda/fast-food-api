""" Module that contains database setup for development and testing env"""
# third party imports
import os
import psycopg2
from flask import current_app
# local imports
from .db_queries import create_table_queries, drop_table_queries


class DatabaseOperations:
    """ Class that establish database connection,
        create db-tables and destroy db-table
        specifically when testing env is on
    """

    def db_con(self):
        """ Method that initialize db connection with any
            database url from the configurations of the current running app
        """
        conn = psycopg2.connect(current_app.config["DATABASE_URL"])
        return conn

    def create_db_tables(self, db_url):
        """Method that creates database tables for any configuration"""
        # db_url = os.getenv("DATABASE_URL")
        conn = psycopg2.connect(db_url)
        with conn:
            with conn.cursor() as curr:
                for query in create_table_queries:
                    curr.execute(query)
        conn.close()

    def destroy_db_tables(self, db_url):
        """Method that destroyes database tables created for testing env"""
        conn = psycopg2.connect(db_url)
        with conn:
            with conn.cursor() as curr:
                for query in drop_table_queries:
                    curr.execute(query)
        return conn

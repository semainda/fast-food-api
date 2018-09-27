import os
import psycopg2

from .db_queries import create_table_queries, drop_table_queries


def init_connection(db_url):
    """This function initializes the database connection for give db_url"""
    conn = psycopg2.connect(db_url)
    return conn
    
dev_db_url = os.getenv("DATABASE_URL")

def create_dev_db_tables():
    """This function creates database with db_url
    for development or production config"""
    conn = init_connection(dev_db_url)
    cursor = conn.cursor()
    for query in create_table_queries:
        cursor.execute(query)
    conn.commit()
    return conn

# "dbname='fasttest_db' user='postgres' host='127.0.0.1' password='semainda'"  testing db
# "dbname='fastfoodfast_db' user='postgres' host='127.0.0.1' password='semainda'"  development db


test_db_url = os.getenv("TEST_DATABASE_URL")


def create_test_db_tables():
    """This function create database tables for testing purposes
    but before it does destroyes the exsisting one"""
    conn = init_connection(test_db_url)
    destroy_db_tables()
    cursor = conn.cursor()
    for query in create_table_queries:
        cursor.execute(query)
    conn.commit()
    return conn


def destroy_db_tables():
    """This function destroyes database database created for testing purposes"""
    conn = init_connection(test_db_url)
    cursor = conn.cursor()
    for query in drop_table_queries:
        cursor.execute(query)
    conn.commit()



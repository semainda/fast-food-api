"""This module contains SQL Queries for both CREATE and DROP database tables for API_V2"""
# Create database queries

users = """CREATE TABLE IF NOT EXISTS users(
                    user_id serial PRIMARY KEY,
                    first_name varchar(30) NOT NULL,
                    last_name varchar(30) NOT NULL,
                    email varchar(30) NOT NULL,
                    user_name  varchar(30) UNIQUE NOT NULL,
                    user_role varchar(20) DEFAULT 'user' NOT NULL,
                    authenticated bool DEFAULT FALSE,
                    password varchar(300) NOT NULL,
                    created_date date NOT NULL);"""

categories = """CREATE TABLE IF NOT EXISTS categories(
                    cat_id serial PRIMARY KEY,
                    cat_name varchar(50) UNIQUE NOT NULL);"""

meals = """CREATE TABLE IF NOT EXISTS meals(
                    meal_id serial PRIMARY KEY,
                    meal_name varchar(50) NOT NULL,
                    cat_id int REFERENCES categories(cat_id) ON DELETE CASCADE ON UPDATE CASCADE,
                    description varchar(80) NOT NULL,
                    price  int  NOT NULL);"""

orders = """CREATE TABLE IF NOT EXISTS orders(
                    order_id serial PRIMARY KEY,
                    user_id int REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
                    status int DEFAULT 0,
                    delivery_address text,
                    created_date date NOT NULL);"""

orders_items = """CREATE TABLE IF NOT EXISTS orders_items(
                    order_id int REFERENCES orders(order_id) ON DELETE CASCADE,
                    meal_id int  REFERENCES meals(meal_id) ON DELETE RESTRICT,
                    quantity int NOT NULL,
                    description  varchar(80) NOT NULL,
                    PRIMARY KEY(order_id, meal_id));"""

create_table_queries = [users, categories, meals, orders, orders_items]


# Drop database queries

users ="DROP TABLE IF EXISTS users CASCADE;"
categories ="DROP TABLE IF EXISTS categories CASCADE;"
meals = "DROP TABLE IF EXISTS meals CASCADE;"
orders ="DROP TABLE IF EXISTS orders CASCADE;"
orders_items ="DROP TABLE IF EXISTS orders_items CASCADE;"

drop_table_queries = [users, categories, meals, orders, orders_items]
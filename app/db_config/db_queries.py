"""This module contains SQL Queries for both CREATE and DROP database tables for API_V2"""
# Create database queries

users = """CREATE TABLE IF NOT EXISTS users(
                    user_id serial PRIMARY KEY,
                    first_name varchar(30) NOT NULL,
                    last_name varchar(30) NOT NULL,
                    email varchar(30) NOT NULL,
                    user_name  varchar(30) UNIQUE NOT NULL,
                    password varchar(300) NOT NULL,
                    created_at date NOT NULL);"""

categories = """CREATE TABLE IF NOT EXISTS categories(
                    cat_id serial PRIMARY KEY,
                    cat_name varchar(50) UNIQUE NOT NULL);"""

meals = """CREATE TABLE IF NOT EXISTS meals(
                    meal_id serial PRIMARY KEY,
                    meal_name varchar(50) NOT NULL,
                    cat_id int REFERENCES categories(cat_id) ON DELETE CASCADE,
                    description varchar(80) NOT NULL,
                    price  int  NOT NULL);"""

orders = """CREATE TABLE IF NOT EXISTS orders(
                    order_id serial PRIMARY KEY,
                    user_id int REFERENCES users(user_id) ON DELETE CASCADE,
                    delivery_address text DEFAULT NULL,
                    description text DEFAULT NULL,
                    created_date date NOT NULL,
                    delivery_time timestamp DEFAULT NULL);"""

orders_items = """CREATE TABLE IF NOT EXISTS orders_items(
                    order_id int REFERENCES orders(order_id) ON DELETE CASCADE,
                    meal_id int  REFERENCES meals(meal_id) ON DELETE RESTRICT,
                    quantity int NOT NULL,
                    PRIMARY KEY(order_id, meal_id));"""

roles = """CREATE TABLE IF NOT EXISTS roles(
                    role_id serial PRIMARY KEY,
                    role_name  varchar(20) DEFAULT 'user' NOT NULL);"""

user_roles = """CREATE TABLE IF NOT EXISTS user_roles(
                    id serial PRIMARY KEY,
                    role_id int REFERENCES roles(role_id) ON DELETE CASCADE,
                    user_id int REFERENCES users(user_id) ON DELETE CASCADE);"""

status = """CREATE TABLE IF NOT EXISTS status(
                status_id serial PRIMARY KEY,
                status_name varchar(20) NOT NULL);"""

order_status = """CREATE TABLE IF NOT EXISTS order_status(
                id serial PRIMARY KEY,
                order_id int REFERENCES orders(order_id),
                status_id int REFERENCES status(status_id));"""


from datetime import datetime
from passlib.hash import pbkdf2_sha256 as hash256
paswd = hash256.hash('admin')
created_date = datetime.now().strftime("%Y-%m-%d")
create_admin = """WITH role AS(
                    INSERT INTO roles(role_name) VALUES('admin') RETURNING role_id
                ), new_user AS(
                    INSERT INTO users(first_name, last_name, email, user_name,
                    password, created_at)
                SELECT 'admin', 'admin', 'admin@admin.com', 'admin', 'admin', '2018-10-5' RETURNING user_id
                )
                INSERT INTO user_roles(role_id, user_id)
                SELECT role.role_id, new_user.user_id FROM role, new_user;"""

create_table_queries = [users, categories, meals,
    orders, orders_items, roles, user_roles, status, order_status]


# Drop database queries

users ="DROP TABLE IF EXISTS users CASCADE;"
categories ="DROP TABLE IF EXISTS categories CASCADE;"
meals = "DROP TABLE IF EXISTS meals CASCADE;"
orders ="DROP TABLE IF EXISTS orders CASCADE;"
orders_items ="DROP TABLE IF EXISTS orders_items CASCADE;"
roles ="DROP TABLE IF EXISTS roles CASCADE;"
user_roles ="DROP TABLE IF EXISTS user_roles CASCADE;"
order_status ="DROP TABLE IF EXISTS order_status CASCADE;"

drop_table_queries = [users, categories, meals,
    orders, orders_items, roles, user_roles, order_status]
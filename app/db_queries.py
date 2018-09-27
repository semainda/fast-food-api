"""This module contains SQL Queries for both CREATE and DROP database tables for API_V2"""
# Create database queries

create_tb1 = """CREATE TABLE IF NOT EXISTS users(
                    user_id serial PRIMARY KEY,
                    first_name varchar(30) NOT NULL,
                    last_name varchar(30) NOT NULL,
                    email varchar(30) NOT NULL,
                    user_name  varchar(30) UNIQUE NOT NULL,
                    user_role int DEFAULT 0 NOT NULL,
                    password varchar(300) NOT NULL,
                    created_date date NOT NULL);"""

create_tb2 = """CREATE TABLE IF NOT EXISTS categories(
                    cat_id serial PRIMARY KEY,
                    cat_name varchar(50) UNIQUE NOT NULL);"""

create_tb3 = """CREATE TABLE IF NOT EXISTS meals(
                    meal_id serial PRIMARY KEY,
                    meal_name varchar(50) NOT NULL,
                    cat_id int REFERENCES categories(cat_id),
                    description varchar(80) NOT NULL,
                    price  int  NOT NULL);"""

create_tb4 = """CREATE TABLE IF NOT EXISTS orders(
                    order_id serial PRIMARY KEY,
                    user_id int REFERENCES users(user_id) ON DELETE CASCADE,
                    status int DEFAULT 0,
                    delivery_address text,
                    created_date date NOT NULL);"""

create_tb5 = """CREATE TABLE IF NOT EXISTS orders_items(
                    order_id int REFERENCES orders(order_id) ON DELETE CASCADE,
                    meal_id int  REFERENCES meals(meal_id) ON DELETE RESTRICT,
                    quantity int NOT NULL,
                    description  varchar(80) NOT NULL,
                    PRIMARY KEY(order_id, meal_id));"""
                    
create_table_queries = [create_tb1, create_tb2, create_tb3, create_tb4, create_tb5]


# Drop database queries

drop_tb1 ="DROP TABLE IF EXISTS users CASCADE;"
drop_tb2 ="DROP TABLE IF EXISTS categories CASCADE;"
drop_tb3 = "DROP TABLE IF EXISTS meals CASCADE;"
drop_tb4 ="DROP TABLE IF EXISTS orders CASCADE;"
drop_tb5 ="DROP TABLE IF EXISTS orders_items CASCADE;"

drop_table_queries = [drop_tb1, drop_tb2, drop_tb3, drop_tb4, drop_tb5]
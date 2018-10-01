# Fast-food-Apis

## Introduction

This is an api application compaises of several end points for a food delivery service app.

[![Build Status](https://travis-ci.com/semainda/fast-food-api.svg?branch=ft-delete-order-%23160535015)](https://travis-ci.com/semainda/fast-food-api)
[![Maintainability](https://api.codeclimate.com/v1/badges/24d19424862c6612cb7d/maintainability)](https://codeclimate.com/github/semainda/fast-food-api/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/semainda/fast-food-api/badge.svg)](https://coveralls.io/github/semainda/fast-food-api)

## Run in Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/725e0595dfb78654b40f)

## Features Included

1. Register a user
2. Login a user
3. Place an order for food
4. Get order history for a perticular user
5. Get all orders
6. Add a specific order
7. Update the status of an order
8. Add menu category
9. Update a specific menu category
10. Delete a specific menu category
11. Get available menu
12. Add meal option to the menu

## Prerequisite

### Installation

#### Step 1: Create a project directory

```$ mkdir fast-food-api```

```$ cd fast-food-api```

#### Step 2: Created virtual enviroment

```$ apt get install pipenv```

```$ pipenv --python 3.6```

#### Step 3: Activate the virtual envinment

```$ pipenv shell```

#### Step 4: Clone the fast-food-api repository

[```here```](https://github.com/semainda/fast-food-api) or ```git clone https://github.com/semainda/fast-food-api```


#### Step 5: Install project dependances

```$ pipenv install```

### Exporting environment variable

#### For development purposes

```$ export APP_SETTINGS = "development"```

#### For testing purposes

```$ export APP_SETTINGS = "testing"```

### Running the application

```$ python run.py```

### Running the Tests

```$ pytest app/tests"```

## Users API - Endpoints: /api/v2/

Method | Endpoint | Functionality
----| ---- | ---
POST | /auth/signup | Register a user
POST  | /auth/login | Login a user
POST  | /auth/logout | Sign out a user

## Orders API - Endpoints: /api/v2/

Method | Endpoint | Functionality
----| ---- | ---
POST | users/orders | Place and order for food
GET  | users/orders | Get the order history for a perticular user
GET  | /orders/ | Get all orders
GET  | /orders/order_id | Add a specific order
PUT  | /orders/order_id | Updated the status of an order
GET  |  /menu | Get available menu
POST | /menu  | Add a meal option to the menu
POST | /menu/categories/ | Add a menu category
GET  | /menu/categories | Get all categories
GET  | /menu/categories/cat_id | Get a specific category
PUT  |/menu/categories/cat_id | Update a specific category
DELETE  |/menu/categories/cat_id | Delete a specific category

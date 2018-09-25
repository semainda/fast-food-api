# Fast-food-Apis

## Introduction

This is an api application compaises of several end points for a food delivery service app.

[![Build Status](https://travis-ci.com/semainda/fast-food-api.svg?branch=ft-delete-order-%23160535015)](https://travis-ci.com/semainda/fast-food-api)
[![Test Coverage](https://api.codeclimate.com/v1/badges/24d19424862c6612cb7d/test_coverage)](https://codeclimate.com/github/semainda/fast-food-api/test_coverage)

## Run in Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/725e0595dfb78654b40f)

## Features Included

1. Create order
2. View a list of all orders
3. View a specific order
4. Updated a specific order
5. Delete a specific order

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

## API - Endpoints: /api/v1/

Method | Endpoint | Functionality
----| ---- | ---
POST | /orders | Create order
GET  | /orders | View a list of all orders
GET  | /orders/int:order_id | View a specific order
PUT  | /orders/int:order_id | Updated a specific order
DELETE | Updated a specific order | Delete a specific order

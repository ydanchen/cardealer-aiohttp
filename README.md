# Car Dealers API | Python AQA Homework
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/ydanchen/cardealer-aiohttp) 
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/ydanchen/cardealer-aiohttp/aiohttp)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/ydanchen/cardealer-aiohttp/apscheduler)


Simple asynchronous REST API with Python aiohttp library.

The following toolset was used:
* Python 3.9
* pipenv
* aiohttp
* sqlite3
* apscheduler

Tables:
* dealer(id, name)
* car(id, modelName, color, dealerId)

There are two endpoints:
* `/dealers`
    * add - `POST` method
    * delete - `DELETE` method, path param, e.g. `/dealers/1`
    * list - `GET` method
* `/cars`
    * add - `POST` method
    * delete - `DELETE` method, path param, e.g. `/cars/1`
    * list - `GET` method
    * list with filters by color, model - `GET` method with query parameters, e.g.: `/cars?color=White`

Database already seeded with fake data. To re-seed DB, use `seed_db.py`. Sync between the DB and API is configured
to perform every 10 seconds.

Run server:
```bash
$ ./run.sh
```

## Requests
List cars:
```bash
curl --request GET 'http://localhost:5000/cars'
```
List cars with a filter:
```bash
curl --request GET 'http://localhost:5000/cars?color=White'
```
Add a car:
```bash
curl --request POST 'http://localhost:5000/cars' \
--header 'Content-Type: application/json' \
--data-raw '{
    "brand": "Wooling",
    "model": "Cheetah",
    "color": "Pink",
    "dealer_id": 1
}'
```
Delete a car:
```bash
curl --request DELETE 'http://localhost:5000/cars/1'
```
List dealers:
```bash
curl --request GET 'http://localhost:5000/dealers'
```
Add a dealer:
```bash
curl --request POST 'http://localhost:5000/dealers' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "KyivAutoTorg",
    "address": "Ukraine, Kyiv, Maidan Nezalezhnosti square, 1"
}'
```
Delete a dealer:
```bash
curl --request DELETE 'http://localhost:5000/dealers/1'
```

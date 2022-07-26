from aiohttp import web
from aiohttp.web_exceptions import HTTPCreated, HTTPBadRequest

from controller import get_cars, get_car_by_id, store_car, delete_car, get_dealers, store_dealer, delete_dealer
from data.models import is_valid, Car, Dealer
from utils import json_response


async def list_cars(request: web.Request) -> web.Response:
    color_filter = request.rel_url.query.get('color')
    model_filter = request.rel_url.query.get('model')
    return json_response(get_cars(color_filter, model_filter))


async def get_car(request: web.Request) -> web.Response:
    car_id = request.match_info.get('car_id')
    return json_response(get_car_by_id(car_id))


async def add_car(request: web.Request) -> web.Response:
    json = await request.json()
    if is_valid(Car(), json):
        store_car(Car(**json))
        return json_response({'result': 'Success'}, status=HTTPCreated.status_code)
    else:
        raise HTTPBadRequest


async def remove_car(request: web.Request) -> web.Response:
    car_id = request.match_info.get('car_id')
    delete_car(car_id)
    return json_response({'result': 'Success'})


async def list_dealers(request: web.Request) -> web.Response:
    return json_response(get_dealers())


async def add_dealer(request: web.Request) -> web.Response:
    json = await request.json()
    if is_valid(Dealer(), json):
        store_dealer(Dealer(**json))
        return json_response({'result': 'Success'}, status=HTTPCreated.status_code)
    else:
        raise HTTPBadRequest


async def remove_dealer(request: web.Request) -> web.Response:
    dealer_id = request.match_info.get('dealer_id')
    delete_dealer(dealer_id)
    return json_response({'result': 'Success'})

import logging

from aiohttp import web
from apscheduler.schedulers.background import BackgroundScheduler

from data.database import DATABASE
from handlers import list_cars, get_car, remove_car, add_car, list_dealers, add_dealer, remove_dealer

logging.basicConfig(level=logging.DEBUG)

SCHEDULER = BackgroundScheduler(daemon=True)


def commit_transaction():
    DATABASE.commit()


# Commit transactions every 10 seconds
SCHEDULER.add_job(commit_transaction, 'interval', seconds=10)
SCHEDULER.start()

app = web.Application()

app.add_routes([
    web.get('/cars', list_cars),
    web.get('/cars/{car_id}', get_car),
    web.post('/cars', add_car),
    web.delete('/cars/{car_id}', remove_car),
    web.get('/dealers', list_dealers),
    web.post('/dealers', add_dealer),
    web.delete('/dealers/{dealer_id}', remove_dealer)
])

if __name__ == '__main__':
    web.run_app(app, host='localhost', port=5000)

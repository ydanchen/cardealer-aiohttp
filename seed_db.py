from random import choice, randint

from data.database import DataBase
from data.models import Dealer, Car

FIRST_NAME_PART = ['Ukr', 'Avto', 'Biz', 'Bud', 'Motor', 'Oil', 'Vip']
SECOND_NAME_PART = ['Group', 'Deal', 'Auto', 'Center', 'Stroi', 'Prodazha', 'Torg']
CITIES = ['Kyiv', 'Kharkov', 'Lviv', 'Odessa', 'Dnipro', 'Kherson', 'Sumy']
STREETS = ['Shevchenko', 'Heroiv UPA', 'Okruzhnaya', 'Lesi Ukrainki', '1-ya Liniya', '2-ya Liniya']
COLORS = ['Red', 'White', 'Black', 'Gray', 'Yellow', 'Blue', 'Green']
BRANDS = ['ZAZ', 'Daewoo', 'Chevrolet', 'GMC', 'Vauxhall', 'Saab', 'Fiat', 'Luaz', 'Ferrari', 'Lorraine-Dietrich']
MODELS = ['Slavuta', 'Forza', '911', '600SEL', 'Topolino', 'Vectra', '300C', 'A250', 'E400h', 'V40', 'S80', 'E95']


def create_random_dealer() -> Dealer:
    name = f"{choice(FIRST_NAME_PART)}{choice(SECOND_NAME_PART)}"
    address = f"Ukraine, {choice(CITIES)}, {choice(STREETS)} str., {randint(1, 155)}"
    return Dealer(name=name, address=address)


def create_random_car(dealers: int) -> Car:
    return Car(brand=choice(BRANDS), model=choice(MODELS), color=choice(COLORS), dealer_id=randint(1, dealers))


if __name__ == '__main__':
    db = DataBase('data/cars_dealers.db')
    db.execute_script('data/create_db.sql')

    dealers_count = 15

    # Seed fake dealers
    for _ in range(dealers_count):
        dealer = create_random_dealer()
        query = f"INSERT INTO dealers (name, address) VALUES ('{dealer.name}', '{dealer.address}');"
        db.execute(query)

    # Seed fake cars
    for _ in range(100):
        car = create_random_car(dealers_count)
        query = f"INSERT INTO cars (brand, model, color, dealer_id) " \
                f"VALUES('{car.brand}', '{car.model}', '{car.color}', '{car.dealer_id}')"
        db.execute(query)

    db.commit()

from data.database import DATABASE
from data.models import Car, Dealer


def get_cars(color_filter: str, model_filter: str) -> list:
    query = "SELECT id, brand, model, color, dealer_id FROM cars"
    filters = []
    if color_filter:
        filters.append(f"color = '{color_filter}'")
    if model_filter:
        filters.append(f"model = '{model_filter}'")

    if color_filter or model_filter:
        query = query + f" WHERE {' AND '.join(filters)}"

    records = DATABASE.execute(query).fetchall()
    return [Car(id=r[0], brand=r[1], model=r[2], color=r[3], dealer_id=r[4]) for r in records]


def get_car_by_id(car_id: int) -> list:
    query = f"SELECT id, brand, model, color, dealer_id FROM cars WHERE id={car_id}"
    records = DATABASE.execute(query).fetchall()
    return [Car(id=r[0], brand=r[1], model=r[2], color=r[3], dealer_id=r[4]) for r in records]


def store_car(car: Car) -> None:
    query = f"INSERT INTO cars (brand, model, color, dealer_id) " \
            f"VALUES('{car.brand}', '{car.model}', '{car.color}', '{car.dealer_id}')"
    DATABASE.execute(query)


def delete_car(car_id: int) -> None:
    query = f"DELETE from cars WHERE id={car_id}"
    DATABASE.execute(query)


def get_dealers() -> list:
    query = "SELECT id, name, address FROM dealers"
    records = DATABASE.execute(query).fetchall()
    return [Dealer(id=r[0], name=r[1], address=r[2]) for r in records]


def delete_dealer(dealer_id: int) -> None:
    query = f"DELETE from dealers WHERE id={dealer_id}"
    DATABASE.execute(query)


def store_dealer(dealer: Dealer) -> None:
    query = f"INSERT INTO dealers (name, address) " \
            f"VALUES('{dealer.name}', '{dealer.address}')"
    DATABASE.execute(query)

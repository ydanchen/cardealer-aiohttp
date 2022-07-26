class DataObject:
    pass


class Car(DataObject):
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.brand = kwargs.get("brand")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.dealer_id = kwargs.get("dealer_id")

    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"


class Dealer(DataObject):
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.address = kwargs.get("address")

    def __str__(self):
        return f"{self.name}, {self.address}"


def is_valid(dto: DataObject, json: dict) -> bool:
    fields = dto.__dict__
    del fields['id']
    for field in fields:
        if field not in json:
            return False
    return True

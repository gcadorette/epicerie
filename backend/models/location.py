from backend.models.model import Model

class Location(Model):
    def __init__(self, _country, _state, _city, _civicNumber, _street, _suite, _chain):
        self.country = _country
        self.state = _state
        self.city = _city
        self.civicNumber = _civicNumber
        self.street = _street
        self.suite = _suite
        self.chain = _chain
        super().__init__()
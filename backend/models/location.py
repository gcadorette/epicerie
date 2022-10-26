from dataclasses import dataclass
from models.model import Model

@dataclass
class Location(Model):
    country: str
    state: str
    city: str
    civic_number: str
    street: str
    suite: str
    chain_id: str

    def __init__(self, country: str, state: str, city: str, civic_number: str, street: str, suite: str, chain_id: str):
        self.country = country
        self.state = state
        self.city = city
        self.civic_number = civic_number
        self.street = street
        self.suite = suite
        self.chain_id = chain_id
        super().__init__()
        
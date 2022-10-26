from dataclasses import dataclass
import datetime
from models.model import Model

@dataclass
class Price(Model):
    amount: int
    date: datetime
    is_special: bool
    product_id: str
    location_id: str

    def __init__(self, amount: int, date: datetime, is_special: str, product_id: str, location_id: str, guid: str = None):
        self.amount = amount
        self.date = date
        self.is_special = is_special
        self.product = product_id
        self.location_id = location_id
        super().__init__(guid)

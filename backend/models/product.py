from dataclasses import dataclass
from models.model import Model

@dataclass
class Product(Model):
    name: str
    qte: int
    brand_id: str
    def __init__(self, name: str, qte: int, brand_id: str, guid: str = None):
        self.name = name
        self.qte = qte
        self.brand_id = brand_id
        super().__init__(guid)
        
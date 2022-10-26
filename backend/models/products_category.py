from dataclasses import dataclass
from models.model import Model

@dataclass
class ProductsCategory(Model):
    category_id: str
    product_id: str

    def __init__(self, category_id: str, product_id: str):
        self.category_id = category_id
        self.product = product_id
        super().__init__()

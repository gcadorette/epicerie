from models.brand import Brand
from models.product import Product

class IClient:
    def add_product(self, product: Product) -> None:
        pass
    def products(self) -> list:
        pass
    def add_brand(self, brand: Brand) -> None:
        pass
    def brands(self) -> list:
        pass

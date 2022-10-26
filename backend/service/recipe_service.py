from client.iclient import IClient
from models.brand import Brand
from models.product import Product

class RecipeService:
    _client: IClient = None

    def __init__(self, client: IClient):
        self._client = client

    def add_product(self, product: Product) -> None:
        self._client.add_product(product)

    def get_all_products(self) -> list:
        return self._client.products()

    def add_brand(self, brand: Brand) -> None:
        self._client.add_brand(brand)

    def get_all_brands(self) -> list:
        return self._client.brands

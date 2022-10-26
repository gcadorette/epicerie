from client.iclient import IClient
from models.product import Product

class ProductService:
    _client: IClient = None

    def __init__(self, client: IClient):
        self._client = client

    def add_product(self, product: Product) -> None:
        self._client.add_product(product)

    def get_all_products(self) -> list:
        return self._client.products()

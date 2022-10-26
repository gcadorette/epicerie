from client.file_client import FileClient
from models.product import Product
from service.product_service import ProductService


if __name__ == "__main__":
    client = FileClient()
    service = ProductService(client)
    product = Product("test1", 1, "test2")
    service.add_product(product)
    all_products = service.get_all_products()
    print(all_products)
    
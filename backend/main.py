from client.file_client import FileClient
from models.brand import Brand
from models.product import Product
from service.recipe_service import RecipeService

if __name__ == "__main__":
    client = FileClient()
    service = RecipeService(client)

    brand = Brand("President Choice")
    service.add_brand(brand)

    product = Product("biscuit décadents", 300, brand.guid)
    service.add_product(product)
    all_products = service.get_all_products()
    print(all_products)

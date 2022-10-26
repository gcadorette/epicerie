from enum import Enum

from client.iclient import IClient
from constants import Constants
from models.brand import Brand
from models.model import Model
from models.product import Product

class File(Enum):
    PRODUCT = 'product.csv'
    BRAND = 'brand.csv'
    LOCATION = 'location.csv'
    PRICE = 'price.csv'
    CHAIN = 'chain.csv'
    CAT_PROD = 'cat_prod.csv'
    CATEGORY = 'category.csv'
    CATEGORY_NODE = 'category_node.csv'

class FileClient(IClient):
    def add_product(self, product: Product) -> None:
        self._add_to_file(File.PRODUCT, product)

    def add_brand(self, brand: Brand) -> None:
        self._add_to_file(File.BRAND, brand)

    def products(self) -> list:
        return self._get_models_from_file(File.PRODUCT, Product.__name__)

    def brands(self) -> list:
        return self._get_models_from_file(File.BRAND, Brand.__name__)

    def _add_to_file(self, file_name: Enum, obj_to_add: Model) -> None:
        with open(f"{Constants.test_data_folder}/{file_name.value}", "a", encoding="utf-8") as f:
            f.write(obj_to_add.to_csv_string())

    def _get_models_from_file(self, file_name: Enum, type_of_model: str) -> list:
        values = []
        with open(f"{Constants.test_data_folder}/{file_name.value}", "r", encoding="utf-8") as f:
            lines = f.readlines()
            class_type = globals()[type_of_model]
            keys = lines[0].rstrip().replace("\n", "").split(",")
            for line in lines[1:]:
                obj = {}
                vals = line.rstrip().replace("\n", "").split(",")
                if vals:
                    for i in range(len(vals)):
                        obj[keys[i]] = vals[i]
                    values.append(class_type(**obj))
        return values

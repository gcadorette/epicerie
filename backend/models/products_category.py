from backend.models.model import Model

class ProductsCategory(Model):
    def __init__(self, _category, _product):
        self.category = _category
        self.product = _product
        super.__init__()
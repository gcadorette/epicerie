from backend.models.model import Model

class Product(Model):
    id = None
    def __init__(self, _name, _qte, _brand):
        self.name = _name
        self.qte = _qte
        self.brand = _brand
        super().__init__()
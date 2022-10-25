from model import Model

class Price(Model):
    def __init__(self, _amount, _date, _is_special, _product, _location):
        self.amount = _amount
        self.date = _date
        self.is_special = _is_special
        self.product = _product
        self.location = _location
        super().__init__()

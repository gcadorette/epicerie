from model import Model

class Price(Model):
    def __init__(self, _amount, _date, _isSpecial, _product, _location):
        self.amount = _amount
        self.date = _date
        self.isSpecial = _isSpecial
        self.product = _product
        self.location = _location
        super().__init__()
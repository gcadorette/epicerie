from model import Model

class Brand(Model):
    def __init__(self, _name):
        self.name = _name
        super().__init__()
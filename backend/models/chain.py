from backend.models.model import Model

class Chain(Model):
    def __init__(self, _name):
        self.name = _name
        super().__init__()
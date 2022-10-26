from dataclasses import dataclass
from models.model import Model

@dataclass
class Brand(Model):
    name: str
    def __init__(self, name: str):
        self.name = name
        super().__init__()

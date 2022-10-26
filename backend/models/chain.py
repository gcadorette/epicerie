from dataclasses import dataclass
from models.model import Model

@dataclass
class Chain(Model):
    name: str
    def __init__(self, name: str, guid: str = None):
        self.name = name
        super().__init__(guid)
        
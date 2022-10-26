from dataclasses import dataclass
from models.model import Model

@dataclass
class CategoryNode(Model):
    child_id: str
    parent_id: str
    def __init__(self, child_id: str, parent_id: str ="", guid: str = None):
        self.child = child_id
        self.parent = parent_id
        super().__init__(guid)
        
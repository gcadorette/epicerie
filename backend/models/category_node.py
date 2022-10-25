from model import Model

class CategoryNode(Model):
    def __init__(self, _child, _parent=None):
        self.child = _child
        self.parent = _parent
        super().__init__()
        
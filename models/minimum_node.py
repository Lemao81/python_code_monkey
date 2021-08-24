from models.node import Node


class MinimumNode(Node):
    def __init__(self, id: int, value: int, mininum: int):
        Node.__init__(self, id, value)
        self.minimum = mininum

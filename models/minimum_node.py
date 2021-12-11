from models.linked_list_node import LinkedListNode


class MinimumNode(LinkedListNode):
    def __init__(self, id: int, value: int, mininum: int):
        LinkedListNode.__init__(self, id, value)
        self.minimum = mininum

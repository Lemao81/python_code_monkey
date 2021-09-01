from models.minimum_node import MinimumNode


class Stack:
    def __init__(self):
        self._node_id_increment = 0
        self._head = None
        self.count = 0

    def push(self, value):
        minimum = value if self._head is None else min(value, self._head.minimum)
        new_node = MinimumNode(self._node_id_increment, value, minimum)
        new_node.next = self._head
        self._head = new_node
        self._node_id_increment += 1
        self.count += 1

    def pop(self):
        if self._head is None:
            raise ValueError
        value = self._head.value
        self._head = self._head.next
        self.count -= 1
        return value

    def peek(self):
        if self._head is None:
            raise ValueError
        return self._head.value

    def clear(self):
        self._head = None
        self.count = 0

    def min(self):
        if self._head is None:
            raise ValueError
        return self._head.minimum

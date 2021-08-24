from models.minimum_node import MinimumNode


class Stack2:
    def __init__(self):
        self._node_id_increment = 0
        self.head = None

    def push(self, value):
        minimum = value if self.head is None else min(value, self.head.minimum)
        new_node = MinimumNode(self._node_id_increment, value, minimum)
        new_node.next = self.head
        self.head = new_node
        self._node_id_increment += 1

    def pop(self):
        if self.head is None:
            raise ValueError
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if self.head is None:
            raise ValueError
        return self.head.value

    def clear(self):
        self.head = None

    def count(self) -> int:
        count = 0
        runner = self.head
        while runner is not None:
            count += 1
            runner = runner.next
        return count

    def min(self):
        if self.head is None:
            raise ValueError
        return self.head.minimum

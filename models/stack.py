from models.data_node import DataNode


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = DataNode(value)
        new_node.next = self.head
        self.head = new_node

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

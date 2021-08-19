from models.data_node import DataNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = DataNode(value)
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

        pass

    def pop(self):
        if self.head is None:
            raise ValueError
        value = self.head.value
        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        return value

    def peek(self):
        if self.head is None:
            raise ValueError
        return self.head.value

    def clear(self):
        self.head = self.tail = None

    def count(self) -> int:
        count = 0
        runner = self.head
        while runner is not None:
            count += 1
            runner = runner.next
        return count

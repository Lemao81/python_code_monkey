from models.data_node import DataNode
from typing import TypeVar, Generic

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self._head = None
        self._tail = None
        self.count = 0

    def enqueue(self, value: T):
        node = DataNode(value)
        if self._tail is None:
            self._tail = self._head = node
        else:
            self._tail.next = node
            self._tail = self._tail.next
        self.count += 1

    def dequeue(self) -> T:
        if self._head is None:
            raise ValueError
        value = self._head.value
        if self._head.next is None:
            self._head = self._tail = None
        else:
            self._head = self._head.next
        self.count -= 1
        return value

    def peek(self) -> T:
        if self._head is None:
            raise ValueError
        return self._head.value

    def is_empty(self):
        return self.count == 0

    def clear(self):
        self._head = self._tail = None
        self.count = 0

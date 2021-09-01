from models.stack import Stack


class StackQueue:
    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()
        self._loaded = True

    def enqueue(self, value):
        if not self._loaded:
            self._reload()
        self._stack1.push(value)

    def dequeue(self):
        if not self._loaded:
            return self._stack2.pop()
        self._unload()
        return self._stack1.pop()

    def peek(self):
        self._unload()
        value = self._stack1.peek()
        self._reload()
        return value

    def count(self):
        return self._stack1.count if self._loaded else self._stack2.count

    def _unload(self):
        while self._stack1.count > 1:
            self._stack2.push(self._stack1.pop())
        self._loaded = False

    def _reload(self):
        while self._stack2.count > 0:
            self._stack1.push(self._stack2.pop())
        self._loaded = True

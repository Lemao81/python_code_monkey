from models.stack import Stack


class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self._temp = Stack()

    def push(self, value):
        if not self.is_empty():
            while not self.is_empty() and self.peek() < value:
                self._temp.push(self.pop())
        super().push(value)
        self._unload_temp()

    def _unload_temp(self):
        while not self._temp.is_empty():
            super().push(self._temp.pop())

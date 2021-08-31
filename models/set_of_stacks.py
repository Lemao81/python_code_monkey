from models.stack import Stack


class SetOfStacks:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._current_stack = Stack()
        self._current_stack_count = 0
        self._stacks = Stack()
        self._stacks.push(self._current_stack)

    def push(self, value):
        if self._current_stack_count >= self._capacity:
            self._current_stack = Stack()
            self._stacks.push(self._current_stack)
            self._current_stack_count = 1
        else:
            self._current_stack_count += 1
        self._current_stack.push(value)

    def pop(self):
        if self._current_stack_count >= 1:
            self._current_stack_count -= 1
        else:
            self._current_stack = self._stacks.pop()
        return self._current_stack.pop()

class IndexedSubStack:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._count = 0
        self._values = []

    def push(self, value):
        if self._count >= self._capacity:
            raise ValueError
        self._count += 1
        self._values.append(value)

    def pop(self):
        if self._count <= 0:
            raise ValueError
        self._count -= 1
        value = self._values[self._count]
        self._values = self._values[:-1]
        return value

    def has_capacity(self):
        return self._count < self._capacity

    def is_empty(self):
        return self._count <= 0


class IndexedSetOfStacks:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._current_stack = IndexedSubStack(capacity)
        self._stacks = [self._current_stack]

    def push(self, value):
        sub_stack_with_capacity = next((stack for stack in self._stacks if stack.has_capacity()), None)
        if sub_stack_with_capacity is None:
            self._current_stack = IndexedSubStack(self._capacity)
            self._stacks.append(self._current_stack)
            sub_stack_with_capacity = self._current_stack
        sub_stack_with_capacity.push(value)

    def pop(self):
        if self._current_stack.is_empty() and len(self._stacks) == 1:
            raise ValueError
        elif self._current_stack.is_empty():
            self._stacks.remove(self._current_stack)
            self._current_stack = self._stacks[len(self._stacks) - 1]
        return self._current_stack.pop()

    def pop_at(self, index: int):
        value = self._stacks[index].pop()
        if self._stacks[index].is_empty():
            self._stacks.remove(self._stacks[index])
        return value

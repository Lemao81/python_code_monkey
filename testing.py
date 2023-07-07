import random


class Node:
    def __init__(self, value: int):
        self.value = value
        self.rank: int = 0
        self.left: Node | None = None
        self.right: Node | None = None

    def insert(self, value: int):
        if value <= self.value:
            self.rank += 1
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
            return
        if self.right is None:
            self.right = Node(value)
        else:
            self.right.insert(value)

    def get_rank_of_number(self, value: int) -> int:
        if value == self.value:
            return self.rank
        if value < self.value:
            if self.left is None:
                return -1
            return self.left.get_rank_of_number(value)
        if self.right is None:
            return -1
        return self.rank + self.right.get_rank_of_number(value) + 1


def track(value: int):
    root.insert(value)


def get_rank_of_number(value: int) -> int:
    return root.get_rank_of_number(value)


root = Node(random.randint(1, 50))
# for x in range(30):
#     track(random.randint(1, 50))
track(5)
track(1)
track(4)
track(4)
track(5)
track(9)
track(7)
track(13)
track(3)

print(get_rank_of_number(1))
print(get_rank_of_number(3))
print(get_rank_of_number(4))

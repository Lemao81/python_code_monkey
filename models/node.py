class Node:
    def __init__(self, id: int, value):
        self.id = id
        self.value = value
        self.next = None

    def __str__(self):
        return f'Id: {self.id}'

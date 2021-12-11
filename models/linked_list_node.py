class LinkedListNode:
    _next_id = 0

    def __init__(self, value):
        self.id = LinkedListNode._next_id
        LinkedListNode._next_id += 1
        self.value = value
        self.next = None

    def __str__(self):
        return f'Id: {self.id}'

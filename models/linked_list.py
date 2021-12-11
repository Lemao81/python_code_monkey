from models.linked_list_node import LinkedListNode


class LinkedList:
    def __init__(self, value):
        self.root = LinkedListNode(value)

    def get_tail(self) -> LinkedListNode:
        head = self.root
        while head.next is not None:
            head = head.next
        return head

    def append(self, value):
        self.get_tail().next = LinkedListNode(value)

    def get_count(self):
        head = self.root
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count

    def print_values(self):
        head = self.root
        while head is not None:
            if head.next is None:
                print(head.value)
            else:
                print(head.value, end=" ")
            head = head.next

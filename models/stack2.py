from models.linked_list_node import LinkedListNode


class Stack2:
    def __init__(self):
        self._node_id_increment = 0
        self._head = None
        self._ascending_head = None

    def push(self, value):
        new_value_node = LinkedListNode(self._node_id_increment, value)
        new_ascending_node = LinkedListNode(self._node_id_increment, value)
        self._node_id_increment += 1
        new_value_node.next = self._head
        self._head = new_value_node
        if self._ascending_head is None:
            self._ascending_head = new_ascending_node
        elif self._ascending_head.value > new_ascending_node.value:
            new_ascending_node.next = self._ascending_head
            self._ascending_head = new_ascending_node
        else:
            runner = self._ascending_head
            while runner.next is not None and new_ascending_node.value > runner.next.value:
                runner = runner.next
            temp = runner.next
            runner.next = new_ascending_node
            new_ascending_node.next = temp

    def pop(self):
        if self._head is None:
            raise ValueError
        node_id = self._head.id
        value = self._head.value
        self._head = self._head.next
        if self._ascending_head.id == node_id:
            self._ascending_head = self._ascending_head.next
        else:
            runner = self._ascending_head
            while runner.next.id != node_id:
                runner = runner.next
            runner.next = runner.next.next

        return value

    def peek(self):
        if self._head is None:
            raise ValueError
        return self._head.value

    def clear(self):
        self._head = None

    def count(self) -> int:
        count = 0
        runner = self._head
        while runner is not None:
            count += 1
            runner = runner.next
        return count

    def min(self):
        if self._ascending_head is None:
            raise ValueError
        return self._ascending_head.value

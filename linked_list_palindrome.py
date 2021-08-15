import math

from models.node import Node
from common import print_linked_list, get_linked_list_length


def create_letter_linked_list(string: str):
    head = None
    tail = None
    for c in string:
        id = 1 if tail is None else tail.id + 1
        node = Node(id, c)
        if tail is None:
            tail = node
            head = node
        else:
            tail.next = node
            tail = tail.next
    return head


def check_is_palindrome(first_node: Node):
    (is_palindrome, _) = is_palindrome_recursive(first_node, '')
    return is_palindrome


def is_palindrome_recursive(first_node: Node, word: str):
    if first_node.next is not None:
        (result, index) = is_palindrome_recursive(first_node.next, word + first_node.value)
    else:
        result = True
        index = 0
    result = False if not result else True if index >= len(word) else first_node.value == word[index]
    index += 1
    return (result, index)


def reverse_linked_list(first_node: Node):
    node_stack = []
    while first_node is not None:
        node_stack.append(Node(first_node.id, first_node.value))
        first_node = first_node.next
    head = node_stack.pop()
    tail = head
    while len(node_stack) > 0:
        tail.next = node_stack.pop()
        tail = tail.next
    tail.next = None
    return head


def check_is_palindrome2(first_node: Node):
    forward = first_node
    reverse = reverse_linked_list(first_node)
    while forward is not None and reverse is not None:
        if forward.value != reverse.value:
            return False
        forward = forward.next
        reverse = reverse.next
    return True


def check_is_palindrome3(first_node: Node):
    length = get_linked_list_length(first_node)
    (is_palindrome, _) = check_is_palindrome3_recursive(first_node, 0, math.floor(length / 2), length % 2 == 0)
    return is_palindrome


def check_is_palindrome3_recursive(current_node: Node, current_index: int, mid_index: int, is_even: bool):
    limit = mid_index - 1 if is_even else mid_index
    if current_index < limit:
        (is_palindrome, runner) = check_is_palindrome3_recursive(current_node.next, current_index + 1, mid_index, is_even)
    else:
        runner = current_node.next if is_even else current_node
        is_palindrome = True
    is_palindrome = is_palindrome and current_node.value == runner.value
    return (is_palindrome, runner.next)


def check_is_palindrome4(first_node: Node):
    slow_runner = first_node
    fast_runner = first_node
    first_half_stack = []
    while fast_runner is not None and fast_runner.next is not None:
        first_half_stack.append(slow_runner.value)
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
    if fast_runner is not None:
        slow_runner = slow_runner.next
    while slow_runner is not None:
        if first_half_stack.pop() != slow_runner.value:
            return False
        slow_runner = slow_runner.next
    return True


if __name__ == '__main__':
    first_node = create_letter_linked_list('anklna')
    print_linked_list('Word:', first_node)
    print()
    reversed_list = reverse_linked_list(first_node)
    print_linked_list('Reversed:', reversed_list)
    print()

    is_palindrome = check_is_palindrome(first_node)
    print('IS palindrome' if is_palindrome else 'Is NOT palindrome')
    print()

    is_palindrome = check_is_palindrome2(first_node)
    print('IS palindrome indeed' if is_palindrome else 'Is indeed NOT palindrome')
    print()

    is_palindrome = check_is_palindrome3(first_node)
    print('IS palindrome indeed' if is_palindrome else 'Is indeed NOT palindrome')
    print()

    is_palindrome = check_is_palindrome4(first_node)
    print('IS palindrome indeed' if is_palindrome else 'Is indeed NOT palindrome')
    print()

import math

from common import create_linked_list, print_linked_list, get_linked_list_length
from models.node import Node


def linked_list_to_number_reverse_order(first_node: Node) -> int:
    number = 0
    factor = 1
    while first_node is not None:
        number += factor * first_node.value
        first_node = first_node.next
        factor *= 10
    return number


def linked_list_to_number_forward_order(first_node: Node) -> int:
    (result, _) = linked_list_to_number_forward_order_recursive(first_node)
    return result


def linked_list_to_number_forward_order_recursive(first_node: Node):
    if first_node.next is not None:
        (number, factor) = linked_list_to_number_forward_order_recursive(first_node.next)
    else:
        number = 0
        factor = 1
    number += factor * first_node.value
    factor *= 10
    return (number, factor)


def number_to_linked_list_reverse_order(number: int) -> Node:
    first_node = None
    head = None
    while number > 0:
        single_digit = number % 10
        number = math.floor(number / 10)
        if head is None:
            head = Node(1, single_digit)
            first_node = head
        else:
            head.next = Node(head.id + 1, single_digit)
            head = head.next
    return first_node


def number_to_linked_list_forward_order(number: int) -> Node:
    (_, _, result) = number_to_linked_list_forward_order_recursive(number)
    return result


def number_to_linked_list_forward_order_recursive(number: int):
    if number > 0:
        (id, node, first_node) = number_to_linked_list_forward_order_recursive(math.floor(number / 10))
    else:
        return (0, None, None)
    single_digit = number % 10
    id += 1
    new_node = Node(id, single_digit)
    if node is not None:
        node.next = new_node
    else:
        first_node = new_node
    return (id, new_node, first_node)


# def sum_number_linked_lists_reverse(first: Node, second: Node):
#     first_node = None
#     result = None
#     carryover = 0
#     while first is not None or second is not None:
#         first_value = 0 if first is None else first.value
#         second_value = 0 if second is None else second.value
#         sum = first_value + second_value + carryover
#         number = sum % 10
#         carryover = math.floor(sum / 10)
#         if result is None:
#             result = Node(1, number)
#             first_node = result
#         else:
#             result.next = Node(result.id + 1, number)
#             result = result.next
#         first = None if first is None else first.next
#         second = None if second is None else second.next
#     if carryover > 0:
#         result.next = Node(result.id + 1, carryover)
#     return first_node

def sum_number_linked_lists_reverse(first: Node, second: Node):
    result = sum_number_linked_lists_reverse_recursive(first, second)
    return result


def sum_number_linked_lists_reverse_recursive(first: Node, second: Node):
    if first is not None and first.next is not None or second is not None and second.next is not None:
        first_next = None if first is None else first.next
        second_next = None if second is None else second.next
        head = sum_number_linked_lists_reverse_recursive(first_next, second_next)
    else:
        head = None
    first_value = 0 if first is None else first.value
    second_value = 0 if second is None else second.value
    sum = first_value + second_value
    number = sum % 10
    carryover = math.floor(sum / 10)
    if carryover > 0:
        if head is None:
            head = Node(1, carryover)
        else:
            runner = head
            while runner.value + carryover > 9:
                runner = runner.next
            runner.value += carryover
    id = 1 if head is None else head.id + 1
    node = Node(id, number)
    node.next = head
    return node


def sum_number_linked_lists_forward(first: Node, second: Node):
    first_length = get_linked_list_length(first)
    second_length = get_linked_list_length(second)
    if first_length < second_length:
        first = pad_linked_list_from_left(first, second_length - first_length, 0)
    else:
        second = pad_linked_list_from_left(second, first_length - second_length, 0)
    (result, carryover) = sum_number_linked_lists_forward_recursive(first, second)
    if carryover > 0:
        node = Node(result.id + 1, carryover)
        node.next = result
        result = node
    return result


def sum_number_linked_lists_forward_recursive(first: Node, second: Node):
    if first.next is not None and second.next is not None:
        (result, carryover) = sum_number_linked_lists_forward_recursive(first.next, second.next)
    else:
        carryover = 0
        result = None
    sum = first.value + second.value + carryover
    number = sum % 10
    carryover = math.floor(sum / 10)
    if result is None:
        result = Node(1, number)
    else:
        node = Node(result.id + 1, number)
        node.next = result
        result = node

    return (result, carryover)


def pad_linked_list_from_left(head: Node, count: int, value: int):
    node = None
    for i in range(count):
        node = Node(head.id - 1, value)
        node.next = head
        head = node
    return node


if __name__ == '__main__':
    first_number = create_linked_list(3)
    print_linked_list('First number reverse:', first_number)
    second_number = create_linked_list(3)
    print_linked_list('Second number reverse:', second_number)
    print()

    sum = linked_list_to_number_reverse_order(first_number) + linked_list_to_number_reverse_order(second_number)
    print(f'Sum (reverse): {sum}')

    print_linked_list('Sum list (reverse):', number_to_linked_list_reverse_order(sum))
    print()

    first_number = create_linked_list(3)
    print_linked_list('First number forward:', first_number)
    second_number = create_linked_list(3)
    print_linked_list('Second number forward:', second_number)

    sum = linked_list_to_number_forward_order(first_number) + linked_list_to_number_forward_order(second_number)
    print(f'Sum (forward): {sum}')

    print_linked_list('Sum list (forward):', number_to_linked_list_forward_order(sum))
    print()

    first_number = create_linked_list(5)
    print_linked_list('First number reverse:', first_number)
    second_number = create_linked_list(3)
    print_linked_list('Second number reverse:', second_number)
    print_linked_list('Sum list inline:', sum_number_linked_lists_reverse(first_number, second_number))
    print()

    first_number = create_linked_list(3)
    print_linked_list('First number forward:', first_number)
    second_number = create_linked_list(5)
    print_linked_list('Second number forward:', second_number)
    print_linked_list('Sum list inline forward:', sum_number_linked_lists_forward(first_number, second_number))
    print()

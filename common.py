import math
import traceback
import logging
import random
import sys

from models.binary_tree import BinaryTree
from models.binary_tree_node import BinaryTreeNode
from models.linked_list_node import LinkedListNode
from typing import List


def get_input(text=None):
    return input() if text is None else input(text)


def exit_with_invalid_input():
    print("Invalid input")
    traceback.print_exc()
    exit(1)


def validate_range(value: int, lower: int, upper: int):
    if value < lower or value > upper:
        exit_with_invalid_input()


def prompt_single_numeric_input(lower: int, upper: int):
    value = 0
    try:
        value = int(input())
    except ValueError:
        exit_with_invalid_input()

    validate_range(value, lower, upper)

    return value


def parse_int(string: str):
    try:
        return int(string)
    except ValueError:
        exit_with_invalid_input()


def validate_length(array: [], length: int):
    if not len(array) == length:
        exit_with_invalid_input()


def prompt_multiple_numeric_input(amount: int, bounds: [(int, int)]):
    bound_count = len(bounds)
    if bound_count != 1 and bound_count != amount:
        exit_with_invalid_input()
    is_single_bound = bound_count == 1
    input_string = get_input()
    splits = input_string.split()
    validate_length(splits, amount)
    result = []
    for i, split in enumerate(splits):
        lower, upper = bounds[0] if is_single_bound else bounds[i]
        parsed = parse_int(split)
        validate_range(parsed, lower, upper)
        result.append(parsed)

    return result


def right_shift_string_extended(string: str):
    if not string:
        return string
    chars = list(string)
    temp1 = None
    for i, char in enumerate(chars):
        temp2 = char
        if temp1 is not None:
            chars[i] = temp1
        temp1 = temp2
    chars[0] = temp1

    return "".join(chars)


def right_shift_string(string: str):
    return string if not string else string[-1] + string[:-1]


def left_shift_string(string: str):
    return string if not string else string[1:] + string[0]


def get_next_rotating_index(current_index: int, array: []):
    return (current_index + 1) % len(array)


def get_logger():
    handler = logging.FileHandler("logs.txt")
    formatter = logging.Formatter("{asctime}  {levelname:8} - {message}", "%Y%m%d %H:%M:%S", style="{")
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger


def process_and_print_test_case_results(test_case_count: int, test_case_func):
    results = []
    for i in range(test_case_count):
        results.append(test_case_func(i))
    for result in results:
        print(result)


def create_random_node():
    node = LinkedListNode(random.randint(0, 9))
    return node


def create_linked_list(count: int):
    global node_id
    node_id = 0
    first_node = create_random_node()
    before_node = first_node
    for i in range(count - 1):
        next_node = create_random_node()
        before_node.next = next_node
        before_node = next_node
    return first_node


def print_linked_list(text: str, first_node: LinkedListNode):
    print(text)
    current_node = first_node
    values = []
    while current_node is not None:
        values.append(str(current_node.value))
        current_node = current_node.next
    print(' '.join(values))


def linked_list_insert_after(before: LinkedListNode, after: LinkedListNode):
    temp = after.next.next
    after.next.next = before.next
    before.next = after.next
    after.next = temp


def get_linked_list_length(first_node: LinkedListNode):
    count = 0
    while first_node is not None:
        first_node = first_node.next
        count += 1
    return count


def get_linked_list_last_node(first_node: LinkedListNode):
    while first_node.next is not None:
        first_node = first_node.next
    return first_node


def create_random_binary_tree(depth: int) -> BinaryTree:
    tree = BinaryTree(random.randint(1, 99))
    for i in range(depth):
        tree.traverse_post_order(_create_left_right_random_binary_tree_nodes)
    return tree


def create_balanced_binary_tree(values: List) -> BinaryTree:
    values.reverse()
    tree = BinaryTree(values.pop())
    _append_binary_tree_nodes_recursive([tree.root], values)
    return tree


def create_binary_search_tree(values: List) -> BinaryTree:
    values.sort()
    (mid, left_part, right_part) = _split_in_mid_left_right(values)
    tree = BinaryTree(mid)
    _append_binary_search_tree_nodes_recursive(tree.root, left_part, right_part)
    return tree


def get_binary_string(number: int) -> str:
    return "{0:b}".format(number)


def print_binary(number: int | float):
    number_norm = number if isinstance(number, int) else int(number)
    print(get_binary_string(number_norm))


def get_full_binary_string(number: int):
    result = ''
    for x in range(sys.getsizeof(int())):
        result = ('0' if number & 1 == 0 else '1') + result
        number >>= 1
    return result


def print_full_binary(number: int):
    print(get_full_binary_string(number))


def binary_counter(number: int) -> int:
    result = 0
    shift = False
    for i in range(number):
        if shift:
            result = result << 1
        else:
            result += 1
    return result


def print_separator():
    print('---------------------')


def _create_left_right_random_binary_tree_nodes(node: BinaryTreeNode):
    if node.left is None:
        node.left = BinaryTreeNode(random.randint(1, 99), node)
    if node.right is None:
        node.right = BinaryTreeNode(random.randint(1, 99), node)


def _append_binary_tree_nodes_recursive(parents: [BinaryTreeNode], values: List):
    new_parents = []
    for parent in parents:
        if len(values) > 0:
            parent.left = BinaryTreeNode(values.pop())
        if len(values) > 0:
            parent.right = BinaryTreeNode(values.pop())
        new_parents.append(parent.left)
        new_parents.append(parent.right)

    if len(values) > 0:
        _append_binary_tree_nodes_recursive(new_parents, values)


def _append_binary_search_tree_nodes_recursive(node: BinaryTreeNode, smaller_values: List, bigger_values: List):
    if node is None:
        return

    (mid, left_part, right_part) = _split_in_mid_left_right(smaller_values)
    node.left = None if mid is None else BinaryTreeNode(mid, node)
    _append_binary_search_tree_nodes_recursive(node.left, left_part, right_part)
    (mid, left_part, right_part) = _split_in_mid_left_right(bigger_values)
    node.right = None if mid is None else BinaryTreeNode(mid, node)
    _append_binary_search_tree_nodes_recursive(node.right, left_part, right_part)


def _split_in_mid_left_right(values: List) -> (int | None, List, List):
    values_length = len(values)
    if values_length == 0:
        return None, [], []

    mid = values.pop((values_length // 2) - 1)
    left_part = list(filter(lambda x: x <= mid, values))
    right_part = list(filter(lambda x: x > mid, values))

    return mid, left_part, right_part


def is_prime_number(number: int) -> bool:
    if number < 2:
        return False
    if number == 2:
        return True
    for x in range(2, number):
        if number % x == 0:
            return False
    return True


def is_divisable(top: int, bottom: int):
    return top % bottom == 0


def is_palindrome(string: str) -> bool:
    half_length = math.ceil(len(string) / 2)
    for x in range(half_length):
        if string[x] != string[len(string) - 1 - x]:
            return False
    return True


def is_palindrome_recursive(string: str) -> bool:
    length = len(string)
    if length == 0 or length == 1:
        return True
    return False if string[0] != string[length - 1] else True and is_palindrome(string[1:-1])


def swap_items(array: list, index1: int, index2: int):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

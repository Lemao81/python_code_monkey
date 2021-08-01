import traceback
import logging
import random

from models.node import Node


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
    global node_id
    node = Node(node_id, random.randint(0, 10))
    node_id += 1
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


def print_linked_list(text: str, first_node: Node):
    print(text)
    current_node = first_node
    values = []
    while current_node is not None:
        values.append(str(current_node.value))
        current_node = current_node.next
    print(' '.join(values))

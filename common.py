import traceback


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
    for i in range(len(splits)):
        lower, upper = bounds[0] if is_single_bound else bounds[i]
        parsed = parse_int(splits[i])
        validate_range(parsed, lower, upper)
        result.append(parsed)

    return result


def right_shift_string_extended(string: str):
    if not string:
        return string
    chars = list(string)
    temp1 = None
    for current in range(len(chars)):
        temp2 = chars[current]
        if temp1 is not None:
            chars[current] = temp1
        temp1 = temp2
    chars[0] = temp1

    return "".join(chars)


def right_shift_string(string: str):
    return string if not string else string[-1] + string[:-1]


def left_shift_string(string: str):
    return string if not string else string[1:] + string[0]


def get_next_rotating_index(current_index: int, array: []):
    return (current_index + 1) % len(array)

import sys
from common import get_full_binary_string, print_full_binary, print_separator
import random


def get_ones_count(number: int):
    count = 0
    for x in range(sys.getsizeof(int())):
        if number & 1 == 1:
            count += 1
        number >>= 1
    return count


def get_next_with_same_ones_count(number: int):
    count = get_ones_count(number)
    increment = number + 1
    while get_ones_count(increment) != count and increment < sys.maxsize:
        increment += 1
    return increment


def get_previous_with_same_ones_count(number: int):
    count = get_ones_count(number)
    decrement = number - 1
    while get_ones_count(decrement) != count and decrement > 0:
        decrement -= 1
    return decrement


def get_first_one_rindex(number: int, rstart: int):
    return get_first_rindex(number, '1', rstart)


def get_first_zero_rindex(number: int, rstart: int):
    return get_first_rindex(number, '0', rstart)


def get_first_rindex(number: int, sign: str, rstart: int):
    binary_string = get_full_binary_string(number)
    return len(binary_string) - 1 - binary_string.rfind(sign, 0, len(binary_string) - rstart)


def flip_bit(number: int, rindex: int):
    xor_mask = 1 << rindex
    return number ^ xor_mask


def bit_to_sign(bit: int) -> str:
    return '0' if bit == 0 else '1'


def get_rsequence_count(number: int, sign: str, rindex: int):
    number = number >> rindex
    total_count = rindex
    count = 0
    while total_count < sys.getsizeof(int()) and bit_to_sign(number & 1) == sign:
        count += 1
        total_count += 1
        number >>= 1
    return count


def print_stats(number: int):
    print(number)
    print_full_binary(number)
    print(get_ones_count(number))
    print_separator()


if __name__ == '__main__':
    number = random.randint(0, sys.maxsize)
    print_stats(number)

    increment_brute_force = get_next_with_same_ones_count(number)
    print_stats(increment_brute_force)

    trailing_zeros_count = get_rsequence_count(number, '0', 0)
    subsequent_ones_count = get_rsequence_count(number, '1', trailing_zeros_count)

    flip_index = trailing_zeros_count + subsequent_ones_count
    increment_operations = ((number ^ (1 << flip_index)) & (~((1 << flip_index) - 1))) | ((1 << (subsequent_ones_count - 1)) - 1)
    print_stats(increment_operations)

    increment_arithmetic = pow(2, trailing_zeros_count) + number + pow(2, subsequent_ones_count - 1) - 1
    print_stats(increment_arithmetic)

    decrement_brute_force = get_previous_with_same_ones_count(number)
    print_stats(decrement_brute_force)

    trailing_ones_count = get_rsequence_count(number, '1', 0)
    subsequent_zeros_count = get_rsequence_count(number, '0', trailing_ones_count)

    flip_index = trailing_ones_count + subsequent_zeros_count
    decrement_operations = ((number ^ (1 << flip_index)) & (~((1 << flip_index) - 1))) | (
            ((1 << (trailing_ones_count + 1)) - 1) << (subsequent_zeros_count - 1))
    print_stats(decrement_operations)

    decrement_arithmetic = number - pow(2, trailing_ones_count) + 1 - pow(2, subsequent_zeros_count - 1)
    print_stats(decrement_arithmetic)

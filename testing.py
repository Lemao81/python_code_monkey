from common import to_binary_string
import math


def count_max_ones_in_row(string: str) -> int:
    max_count = 0
    counter = 0
    for i in range(len(string)):
        if string[i] == '1':
            counter += 1
        else:
            if counter > max_count:
                max_count = counter
            counter = 0
    if counter > max_count:
        max_count = counter
    return max_count


def flip_bit_at(number: int, index: int) -> int:
    return int(number + math.pow(2, index - 1))


def get_max_count_index(number: int, zero_indices: []) -> int:
    index = 0
    max_count = 0
    for x in zero_indices:
        flipped_string = to_binary_string(flip_bit_at(number, x))
        count = count_max_ones_in_row(flipped_string)
        if count > max_count:
            max_count = count
            index = x
    return index


if __name__ == '__main__':
    number = int(input('Number: '))
    binary_string = to_binary_string(number)
    print(binary_string)
    zero_indices = []
    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            zero_indices.append(len(binary_string) - i)
    print(zero_indices)
    print(get_max_count_index(number, zero_indices))

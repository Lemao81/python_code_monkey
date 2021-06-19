alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def get_row_string(row_index: int, reversed_array: [str], width: int):
    string = list(map(lambda x: reversed_array[x if x <= row_index else row_index - (x - row_index)], range(row_index * 2 + 1)))
    return '-'.join(string).center(width, '-')


def print_rangoli(size):
    width = (size * 2 - 1) * 2 - 1
    reversed_array = alphabet[0:size]
    reversed_array.reverse()
    row_strings = list(map(lambda x: get_row_string(x if x < size else size - (x - size) - 2, reversed_array, width), range(size * 2 - 1)))
    print('\n'.join(row_strings))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

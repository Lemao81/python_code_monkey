import math


def find_string(array: list[str], min_index: int, max_index: int, offset: int, search: str):
    def get_new_offset(offset: int) -> int:
        if offset == 0:
            return 1
        if offset < 0:
            return offset * -1 + 1
        return (offset + 1) * -1

    mid_index = math.floor((min_index + max_index) / 2) + offset
    if array[mid_index] == search:
        return mid_index

    if array[mid_index] == '':
        return find_string(array, min_index, max_index, get_new_offset(offset), search)

    if array[mid_index] > search:
        return find_string(array, min_index, mid_index - 1, 0, search)

    return find_string(array, mid_index + 1, max_index, 0, search)


array = ['', '', 'abc', '', 'dft', 'fge', '', '', 'hei', '', 'keo', 'mini', '', '', '', 'pent']
print(find_string(array, 0, len(array) - 1, 0, 'pent'))

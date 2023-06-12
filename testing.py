import math


def binary_search(array: list[int], bottom_index: int, top_index: int, search: int) -> int:
    if bottom_index == top_index and array[bottom_index] != search:
        return -1
    mid_index = math.floor((bottom_index + top_index) / 2)
    if array[mid_index] == search:
        return mid_index
    if array[mid_index] > search:
        return binary_search(array, bottom_index, mid_index, search)
    return binary_search(array, mid_index + 1, top_index, search)


def find_offset(array: list[int]) -> int:
    for x in range(1, len(array) - 1):
        if array[x - 1] > array[x]:
            return x


def binary_search_with_offset(array: list[int], bottom_index: int, top_index: int, offset: int, search: int) -> int:
    if bottom_index == top_index and get_with_offset(array, bottom_index, offset) != search:
        return -1
    mid_index = math.floor((bottom_index + top_index) / 2)
    mid_value = get_with_offset(array, mid_index, offset)
    if mid_value == search:
        return get_offset_index(array, mid_index, offset)
    if mid_value > search:
        return binary_search_with_offset(array, bottom_index, mid_index, offset, search)
    return binary_search_with_offset(array, mid_index + 1, top_index, offset, search)


def get_offset_index(array: list[int], index: int, offset: int) -> int:
    return (index + offset) % len(array)


def get_with_offset(array: list[int], index: int, offset: int) -> int:
    offset_index = get_offset_index(array, index, offset)
    return array[offset_index]


array = [12, 14, 15, 17, 2, 4, 5, 7, 8, 10]
offset = find_offset(array)

print(binary_search_with_offset(array, 0, len(array) - 1, offset, 7))

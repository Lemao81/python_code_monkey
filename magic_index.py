import math
import random

size = 100
min_number = -150
max_number = 150
array_not_distinct = [random.randint(min_number, max_number) for x in range(size)]
array_not_distinct.sort()

array_distinct = []
for x in range(size):
    number = 0
    while number == 0 or number in array_distinct:
        number = random.randint(min_number, max_number)
    array_distinct.append(number)
array_distinct.sort()

non_random_array = [2, 3, 5, 6, 6, 8, 9, 10, 10, 12, 12, 14, 17, 18, 18, 18, 18, 18, 19, 19, 25, 26, 26, 27, 28, 30, 30, 30, 30, 31, 32, 35, 39, 40, 43, 45, 46,
                    47, 47, 50, 55, 57, 58, 59, 60, 62, 63, 64, 64, 64, 64, 65, 66, 68, 72, 73, 74, 78, 80, 82, 84, 86, 86, 88, 88, 89, 89, 92, 93, 94, 95, 98,
                    99, 100, 101, 102, 105, 107, 111, 115, 117, 120, 122, 125, 127, 128, 130, 130, 131, 132, 134, 134, 145, 145, 147, 147, 148, 149, 150, 150]

array_to_chose = array_distinct

print(array_to_chose)


def magic_index_brute_force(array: list[int]) -> int:
    for i, x in enumerate(array):
        if x == i:
            return i
    return -1


def magic_index_recursive(array: list[int], index: int) -> int:
    if index >= len(array):
        return -1
    return index if array[index] == index else magic_index_recursive(array, array[index])


def magic_index_iterative(array: list[int]) -> int:
    index = 0
    while index < len(array):
        if array[index] == index:
            return index
        index = array[index]
    return -1


def magic_index_binary(array: list[int], start: int, end: int) -> int:
    half_index = start + (math.ceil((end - start) / 2))
    half_value = array[half_index]
    if half_value == half_index:
        return half_index
    if end - start < 2:
        return start if array[start] == start else -1
    return magic_index_binary(array, start, half_index - 1) if half_value > half_index else magic_index_binary(array, half_index + 1, end)


print(f'Magic index: {magic_index_brute_force(array_to_chose)}')
# print(f'Magic index: {magic_index_recursive(array_to_chose, 0)}')
# print(f'Magic index: {magic_index_iterative(array_to_chose)}')
print(f'Magic index: {magic_index_binary(array_to_chose, 0, len(array_to_chose) - 1)}')

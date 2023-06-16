def find_length(array: list, start_index: int) -> int:
    if len(array) == 0:
        return 0

    if array[start_index + 1] == -1:
        return 1

    index = 1
    while True:
        if array[start_index + index * 2] == -1:
            break
        index *= 2
    return index + find_length(array, start_index + index)


array = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1]

print(find_length(array, 0))

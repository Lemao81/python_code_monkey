def concat_sorted1(array1: list[int], array2: list[int]) -> list[int]:
    array1_filled_length = len(array1) - len(array2)
    a_walk_count = 0
    a = 0
    b = 0
    while a < len(array1) and b < len(array2):
        if array1[a] > array2[b]:
            offset = 0
            while (b + offset) < len(array2) and array2[b + offset] <= array1[a]:
                offset += 1
            sub_array = array1[a:a + (array1_filled_length - a_walk_count)]
            array1[a + offset:a + offset + len(sub_array)] = sub_array
            array1[a:a + offset] = array2[b:b + offset]
            a += offset + 1
            b += offset
        else:
            a += 1
        a_walk_count += 1

    if b < len(array2) - 1:
        sub_array = array2[b:]
        array1[len(array1) - len(sub_array):] = sub_array

    return array1


def concat_sorted2(array1: list[int], array2: list[int]) -> list[int]:
    pointer1 = 0
    pointer2 = 0
    result = []

    def add_from_1():
        nonlocal pointer1
        result.append(array1[pointer1])
        pointer1 += 1

    def add_from_2():
        nonlocal pointer2
        result.append(array2[pointer2])
        pointer2 += 1

    while pointer1 < len(array1) or pointer2 < len(array2):
        if pointer1 < len(array1):
            if pointer2 < len(array2):
                if array1[pointer1] <= array2[pointer2]:
                    add_from_1()
                else:
                    add_from_2()
            else:
                add_from_1()
        elif pointer2 < len(array2):
            add_from_2()

    return result


def concat_sorted3(array1: list[int], array2: list[int]) -> list[int]:
    last_index_1 = len(array1) - len(array2) - 1
    last_index_2 = len(array2) - 1
    last_index_concat = len(array1) - 1

    while last_index_concat >= 0:
        if last_index_1 >= 0:
            if last_index_2 >= 0:
                if array1[last_index_1] >= array2[last_index_2]:
                    array1[last_index_concat] = array1[last_index_1]
                    last_index_1 -= 1
                else:
                    array1[last_index_concat] = array2[last_index_2]
                    last_index_2 -= 1
            else:
                array1[last_index_concat] = array1[last_index_1]
                last_index_1 -= 1
        elif last_index_2 >= 0:
            array1[last_index_concat] = array2[last_index_2]
            last_index_2 -= 1
        last_index_concat -= 1

    return array1


array1_1: list[int] = [1, 2, 3, 10, 11, 14, 0, 0, 0, 0, 0, 0]
array1_2: list[int] = [1, 2, 3, 10, 11, 14]
array1_3: list[int] = [1, 2, 3, 10, 11, 14, 0, 0, 0, 0, 0, 0]
array2: list[int] = [5, 6, 7, 12, 15, 16]
result1 = concat_sorted1(array1_1, array2)
result2 = concat_sorted2(array1_2, array2)
result3 = concat_sorted3(array1_3, array2)

print(result1)
print(result2)
print(result3)

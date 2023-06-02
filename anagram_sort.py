from common import swap_items


def bubble_sort_string(string: str) -> str:
    return ''.join(bubble_sort(list(string)))


def bubble_sort(array: list) -> list:
    rounds = 0
    while True:
        i = 0
        rounds += 1
        has_swapped = False
        while i < len(array) - 1:
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                has_swapped = True
            i += 1
        if not has_swapped:
            break
    # print(f'Took {rounds} rounds')
    return array


def sort_anagrams(array: list[str]) -> list[str]:
    sorted_strings = list(map(lambda x: bubble_sort_string(x), array))

    candidate_pointer = 0
    while candidate_pointer < len(sorted_strings):
        candidate = sorted_strings[candidate_pointer]
        swap_offset = 1
        for i in range(candidate_pointer + 1, len(sorted_strings)):
            if sorted_strings[i] == candidate:
                swap_items(array, candidate_pointer + swap_offset, i)
                swap_items(sorted_strings, candidate_pointer + swap_offset, i)
                swap_offset += 1
        candidate_pointer += 1
    return array


array = ['intain', 'imeinf', 'aseft', 'aiegmart', 'caiwfpnt', 'iujenmar', 'etafs', 'ienyulrs', 'ienart', 'sftae', 'iniant', 'iefaasrtars']
print(sort_anagrams(array))

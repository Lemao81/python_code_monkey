import itertools

from common import prompt_single_numeric_input, process_and_print_test_case_results, prompt_multiple_numeric_input


def get_permutations(array: [int]) -> [(int, int)]:
    return itertools.combinations(array, 2)


def get_and(permutation: (int, int)) -> int:
    return permutation[0] & permutation[1]


def get_or(permutation: (int, int)) -> int:
    return permutation[0] | permutation[1]


def get_xor(value1: int, value2: int) -> int:
    return value1 ^ value2


def get_minimum_of_bool_expression(permutations: [(int, int)]) -> int:
    mininum = (10 ** 9) + 1
    for permutation in permutations:
        mininum = min(mininum, get_xor(get_and(permutation), get_or(permutation)))

    return mininum


def test_case(_: int) -> int:
    array_size = prompt_single_numeric_input(1, 10 ** 5)
    array = prompt_multiple_numeric_input(array_size, [(0, 10 ** 9)])
    permutations = get_permutations(array)

    return get_minimum_of_bool_expression(permutations)


if __name__ == "__main__":
    test_case_count = prompt_single_numeric_input(1, 10 ** 3)
    process_and_print_test_case_results(test_case_count, test_case)

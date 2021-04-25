import itertools
import cProfile
import timeit

from common import prompt_single_numeric_input, process_and_print_test_case_results


def get_string_number(character_count: int):
    combinations = itertools.product('0123456789', repeat=character_count)
    strings = list(map(lambda x: ''.join(x), combinations))
    filtered_strings = [string for string in strings if "13" not in string]

    return len(filtered_strings)


def get_string_number2(character_count: int):
    if character_count == 1:
        return 10

    combinations = list(itertools.product('0123456789', repeat=character_count))
    count = 0
    combination_length = len(combinations[0])
    for combination in combinations:
        for i in range(combination_length - 1):
            if combination[i] == '1' and combination[i + 1] == '3':
                break
            count = count + 1

    return count


def test_case1(_: int):
    character_count = prompt_single_numeric_input(0, 1000000009)

    return get_string_number(character_count)


def test_case2(_: int):
    character_count = prompt_single_numeric_input(0, 1000000009)

    return get_string_number2(character_count)


def run():
    if __name__ == "__main__":
        test_case_count = prompt_single_numeric_input(1, 100000)
        process_and_print_test_case_results(test_case_count, test_case2)


def run_repeat1():
    get_string_number(3)


def run_repeat2():
    get_string_number2(3)


print(timeit.repeat("run_repeat1()", number=10000, globals=globals()))
print(timeit.repeat("run_repeat2()", number=10000, globals=globals()))

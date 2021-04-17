from common import validate_length, validate_range, exit_with_invalid_input, prompt_single_numeric_input, parse_int


def parse_and_validate_numbers_input(string: str):
    splits = string.split()
    validate_length(splits, 2)
    validate_if_all_numbers(splits)
    validate_range(int(splits[0]), 1, 10 ** 5)
    validate_range(int(splits[1]), 1, 10 ** 6)
    return splits


def validate_if_all_numbers(array: []):
    for n in array:
        try:
            int(n)
        except ValueError:
            exit_with_invalid_input()


def parse_and_validate_array_elements(string: str, element_count: int):
    splits = string.split()
    validate_length(splits, element_count)
    validate_if_all_numbers(splits)
    for part in splits:
        validate_range(parse_int(part), 0, 10 ** 6)
    return splits


def get_new_index(index: int, rotation: int, element_count: int):
    return (index + rotation) % element_count


def execute_test_case():
    count_numbers = parse_and_validate_numbers_input(input())
    element_count = int(count_numbers[0])
    rotation = int(count_numbers[1])
    array_elements = parse_and_validate_array_elements(input(), element_count)
    new_array = [''] * element_count
    for old_index in range(element_count):
        new_array[get_new_index(old_index, rotation, element_count)] = array_elements[old_index]
    print(' '.join(new_array))


test_case_count = prompt_single_numeric_input(1, 20)

for i in range(test_case_count):
    execute_test_case()

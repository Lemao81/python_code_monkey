from common import prompt_single_numeric_input, prompt_multiple_numeric_input, exit_with_invalid_input, left_shift_string, get_next_rotating_index, get_logger

logger = get_logger()


def validate_binary_string(binary_string: str, string_len: int):
    if len(binary_string) != string_len:
        exit_with_invalid_input()
    try:
        int(binary_string, 2)
    except ValueError:
        exit_with_invalid_input()


def count_cyclic_shifts(repeats: int, dec_values: [int], max_value: int):
    cyclic_shift_counter = -1
    max_passed_counter = 0
    index = 0
    while max_passed_counter < repeats:
        if dec_values[index] == max_value:
            max_passed_counter += 1
        index = get_next_rotating_index(index, dec_values)
        cyclic_shift_counter += 1
    return cyclic_shift_counter


def execute_test_case(case_number: int):
    logger.info(f"Starting test case ${case_number + 1}")
    string_len, repeats = prompt_multiple_numeric_input(2, [(1, 10 ** 5), (1, 10 ** 9)])
    binary_string = input()
    validate_binary_string(binary_string, string_len)
    dec_values = []
    max_value = 0
    shifted_string = binary_string
    shifts = []
    for j in range(string_len):
        shifts.append(shifted_string)
        dec_value = int(shifted_string, 2)
        max_value = max(max_value, dec_value)
        dec_values.append(dec_value)
        shifted_string = left_shift_string(shifted_string)

    return count_cyclic_shifts(repeats, dec_values, max_value)


if __name__ == "__main__":
    logger.info("Cyclic shift startet")
    test_case_count = prompt_single_numeric_input(1, 10 ** 3)
    results = []
    for i in range(test_case_count):
        results.append(execute_test_case(i))
    for result in results:
        print(result)
    logger.info("Test case finished")

from common import prompt_multiple_numeric_input, prompt_single_numeric_input


def execute_test_case():
    matrix_size = prompt_single_numeric_input(1, 20)
    matrix_rows = []
    for i in range(matrix_size):
        matrix_rows.append(prompt_multiple_numeric_input(matrix_size, [(1, 1000)]))

    counter = 0
    for row1 in range(matrix_size):
        for column1 in range(matrix_size):
            matrix_entry = matrix_rows[row1][column1]
            for row2 in range(row1, matrix_size):
                for column2 in range(column1, matrix_size):
                    compare_entry = matrix_rows[row2][column2]
                    if compare_entry < matrix_entry:
                        counter += 1
    print(counter)


test_case_count = prompt_single_numeric_input(1, 100)

for i in range(test_case_count):
    execute_test_case()

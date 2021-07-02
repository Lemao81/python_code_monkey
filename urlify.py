def urilify_string(string: str, length: int):
    result = [''] * length
    k = 0
    for i in range(len(string)):
        if string[i].isspace():
            result[k] = '%'
            result[k + 1] = '2'
            result[k + 2] = '0'
            k += 3
        else:
            result[k] = string[i]
            k += 1
    return ''.join(result)


def get_space_count(string):
    count = 0
    for c in string:
        if c.isspace():
            count += 1
    return count


def urilify_string2(string: str, length: int):
    space_count = get_space_count(string)
    result = [''] * (length + 2 * space_count)
    for i in range(len(string)):
        result[i] = string[i]
    string_end_index = length - 1
    result_end_index = len(result) - 1
    for i in range(string_end_index, -1, -1):
        if result[i].isspace():
            result[result_end_index] = '0'
            result[result_end_index - 1] = '2'
            result[result_end_index - 2] = '%'
            result_end_index -= 3
        else:
            result[result_end_index] = result[i]
            result_end_index -= 1
    return ''.join(result)


if __name__ == '__main__':
    string = input()
    length = int(input())
    print(urilify_string2(string, length))

def compress_string(string):
    if not string:
        return ''

    current_char_count = 0
    result = ['']
    for i, c in enumerate(string):
        current_char_count += 1
        if i == len(string) - 1 or string[i + 1] != c:
            result.append(c + str(current_char_count))
            current_char_count = 0
    return ''.join(result) if len(result) < len(string) else string


if __name__ == '__main__':
    string = input()
    print(compress_string(string))

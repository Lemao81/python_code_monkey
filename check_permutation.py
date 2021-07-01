def check_permutation(string1, string2):
    if len(string1) > len(string2):
        return False
    sorted1 = sorted(string1)
    sorted2 = sorted(string2)
    index = 0
    for c in sorted1:
        try:
            index = sorted2.index(c, index) + 1
        except ValueError:
            return False
    return True


def check_permutation2(string1, string2):
    if len(string1) > len(string2):
        return False
    dict = {}
    for c in string2:
        if ord(c) in dict:
            dict[ord(c)] += 1
        else:
            dict[ord(c)] = 1
    for c in string1:
        if ord(c) not in dict or dict[ord(c)] == 0:
            return False
        else:
            dict[ord(c)] -= 1
    return True


def check_permutation3(string1, string2):
    if len(string1) > len(string2):
        return False
    counts = [0] * 128
    for c in string2:
        counts[ord(c)] += 1
    for c in string1:
        counts[ord(c)] -= 1
        if counts[ord(c)] < 0:
            return False
    return True


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    is_permutation = check_permutation3(str1, str2)
    print('Is permutation' if is_permutation else 'Is not a permutation')

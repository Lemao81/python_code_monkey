def is_only_one_replace(string1, string2):
    diff_found = False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if diff_found:
                return False
            else:
                diff_found = True
    return True


def is_only_one_addition(smaller_string, longer_string):
    i = 0
    j = 0
    while i < len(smaller_string):
        if smaller_string[i] != longer_string[j]:
            if i != j:
                return False
            else:
                j += 1
        else:
            i += 1
            j += 1
    return True


def is_one_edit(string1, string2):
    length1 = len(string1)
    length2 = len(string2)
    if string1 == string2 or abs(length1 - length2) > 1:
        return False
    if length1 == length2:
        return is_only_one_replace(string1, string2)
    if length1 < length2:
        return is_only_one_addition(string1, string2)
    if length1 > length2:
        return is_only_one_addition(string2, string1)


def is_one_edit2(string1, string2):
    length1 = len(string1)
    length2 = len(string2)
    if string1 == string2 or abs(length1 - length2) > 1:
        return False

    smaller_one = string2 if length2 < length1 else string1
    bigger_one = string1 if length2 < length1 else string2
    diff_found = False
    i = 0
    j = 0
    while i < len(smaller_one):
        if smaller_one[i] != bigger_one[j]:
            if diff_found:
                return False
            else:
                diff_found = True
                if length1 != length2:
                    j += 1
        else:
            i += 1
            j += 1
    return True


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    print('IS indeed one edit' if is_one_edit2(string1, string2) else 'Is NOT one edit')

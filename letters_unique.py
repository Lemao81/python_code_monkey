def determine_uniqueness(string):
    if not string:
        return True
    if len(string) > 26:
        return False
    distinct = {}
    for c in string:
        lower = c.lower()
        try:
            if distinct[lower]:
                return False
        except KeyError:
            distinct[lower] = True
    return True


def determine_uniqueness2(string):
    if not string:
        return True
    if len(string) > 26:
        return False
    for c in string:
        lower = c.lower()
        if lower in string:
            return False
    return True


def determine_uniqueness3(string):
    if not string:
        return True
    if len(string) > 26:
        return False
    vector = 0
    for c in string:
        lower = c.lower()
        bit = ord(lower) - 97
        if bit < 0 or bit > 122:
            raise ValueError
        shifted = 1 << bit
        if vector & shifted:
            return False
        vector |= shifted
    return True


def determine_uniqueness4(string):
    if not string:
        return True
    if len(string) > 26:
        return False
    sort = sorted(string.lower())
    for i in range(len(sort) - 1):
        if sort[i] == sort[i + 1]:
            return False
    return True


if __name__ == '__main__':
    string = input()
    is_unique = determine_uniqueness4(string)
    print('Unique' if is_unique else 'Not unique')

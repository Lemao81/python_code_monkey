def string_permutation1(string: str, permutations: list[str]):
    if len(string) == 0 or string in permutations:
        return
    permutations.append(string)
    for l in string:
        if string.startswith(l):
            reordered = string
        else:
            reordered = string.replace(l, '')
            reordered = l + reordered
        string_permutation1(reordered, permutations)


def append_permutation(letter: str, permutations: list[str]) -> list[str]:
    new_permutations = []
    if len(permutations) == 0:
        new_permutations.append(letter)
    else:
        current_length = len(permutations[0])
        for i in range(current_length + 1):
            for p in permutations:
                new_permutation = p[:i] + letter + p[i:]
                new_permutations.append(new_permutation)
    return new_permutations


def string_permutation2(string: str) -> list[str]:
    permutations = []
    for l in string:
        permutations = append_permutation(l, permutations)
    return permutations


def append_permutation_recursive(string: str) -> list[str]:
    if len(string) == 1:
        return [string]

    permutations = append_permutation_recursive(string[1:])
    current_length = len(permutations[0])
    new_permutations = []
    for i in range(current_length + 1):
        for p in permutations:
            new_permutation = p[:i] + string[0] + p[i:]
            new_permutations.append(new_permutation)
    return new_permutations


string = 'abcd'

permutations = []
string_permutation1(string, permutations)
print(permutations)

permutations = string_permutation2(string)
print(permutations)

permutations = append_permutation_recursive(string)
print(permutations)
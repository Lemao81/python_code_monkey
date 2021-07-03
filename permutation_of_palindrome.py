import math


def to_lower_alpha(string: str):
    result = []
    for c in string:
        if c.isalpha():
            result.append(c.lower())
    return result


def is_palindrome(string: str):
    length = len(string)
    for i in range(math.floor(length / 2)):
        if string[i].lower() != string[length - 1 - i].lower():
            return False
    return True


def is_alpha(code):
    return (65 <= code <= 90) or (97 <= code <= 122)


def is_single_bit(bit_vector):
    found = False
    for i in range(31):
        if bit_vector & 1 << i:
            if found:
                return False
            found = True
    return found


def is_single_bit2(bit_vector):
    return bit_vector & (bit_vector - 1) == 0


def is_permutation_of_palindrome(string: str):
    hashs = [0] * 90
    for c in string:
        if c.isalpha():
            hashs[ord(c.upper())] += 1
    count_even = 0
    count_odd = 0
    for x in hashs:
        if x > 0:
            if x % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
                if count_odd > 1:
                    return False
    return (count_even > 0 or count_odd > 0) and (count_odd <= 1)


def is_permutation_of_palindrome2(string: str):
    bit_vector = 0
    count_alpha = 0
    for c in string:
        code = ord(c)
        if is_alpha(code):
            normalized = code - 65 if code <= 90 else code - 97
            bit_vector ^= 1 << normalized
            count_alpha += 1
    if count_alpha == 0:
        return False
    return bit_vector == 0 or is_single_bit2(bit_vector)


if __name__ == '__main__':
    string = input()
    print('IS a palindrome permutation' if is_permutation_of_palindrome2(string) else 'Is NOT a permutation of a palindrome')

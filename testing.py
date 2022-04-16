from common import to_binary_string, print_binary


def replace_bits(N: int, M: int, i: int, j: int) -> int:
    mask_init1 = (1 << (j - i + 1)) - 1
    print_binary(mask_init1)
    mask_init2 = mask_init1 << i
    print_binary(mask_init2)
    bit_mask = (1 << 32) - 1 - mask_init2
    print_binary(bit_mask)
    n_masked = N & bit_mask
    n_inserted = n_masked | (M << i)
    print_binary(n_inserted)
    return n_inserted


if __name__ == '__main__':
    N = 2 << 9
    M = 19
    i = 2
    j = 6

    result = to_binary_string(replace_bits(N, M, i, j))
    is_valid = result == "10001001100"

    print("Is valid!!!" if is_valid else f"Is NOT valid: '{result}'")

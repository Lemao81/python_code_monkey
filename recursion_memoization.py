def count_steps_recursive(steps_to_go: int) -> int:
    one_step = count_steps_recursive(steps_to_go - 1) if steps_to_go > 1 else (1 if steps_to_go == 1 else 0)
    two_step = count_steps_recursive(steps_to_go - 2) if steps_to_go > 2 else (1 if steps_to_go == 2 else 0)
    three_step = count_steps_recursive(steps_to_go - 3) if steps_to_go > 3 else (1 if steps_to_go == 3 else 0)

    return one_step + two_step + three_step


def count_steps_memoization(steps_to_go: int, memo: list[int]) -> int:
    if steps_to_go > 1 and memo[steps_to_go - 1] == 0:
        memo[steps_to_go - 1] = count_steps_memoization(steps_to_go - 1, memo)

    one_step = memo[steps_to_go - 1] if steps_to_go > 1 else (1 if steps_to_go == 1 else 0)
    two_step = memo[steps_to_go - 2] if steps_to_go > 2 else (1 if steps_to_go == 2 else 0)
    three_step = memo[steps_to_go - 3] if steps_to_go > 3 else (1 if steps_to_go == 3 else 0)

    return one_step + two_step + three_step


def count_steps_iterative(steps_to_go: int) -> int:
    a = 0
    b = 0
    c = 0
    for x in range(steps_to_go + 1):
        e = 1 if 0 < x < 4 else 0

        d = a + b + c + e
        a = b
        b = c
        c = d
    return c


n = 20

print(str(count_steps_recursive(n)))

memo = [0] * n
print(str(count_steps_memoization(n, memo)))

print(str(count_steps_iterative(n)))

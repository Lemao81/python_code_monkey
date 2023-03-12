def multiply_recursive(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    return b + multiply_recursive(a - 1, b)


def multiply_recursive2(a: int, b: int, results: dict[int]) -> int:
    if a == 0 or b == 0:
        return 0
    if a in results:
        return results[a]
    if a > 1:
        result = 0
        a2 = a
        if a % 2 > 0:
            result += b
            a2 -= 1
        a_half = a2 >> 1
        result += multiply_recursive2(a_half, b, results) + multiply_recursive2(a_half, b, results)
        results[a] = result
        return result
    else:
        results[a] = b
        return b


print(multiply_recursive(125, 237))
print(multiply_recursive2(125, 237, dict()))

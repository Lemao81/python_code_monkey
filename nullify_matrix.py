import math


def nullify_matrix(matrix):
    length = len(matrix[0])
    x_bitvector = 0
    y_bitvector = 0
    for y in range(length):
        for x in range(length):
            if matrix[y][x] == 0:
                y_bitvector |= 1 << y
                x_bitvector |= 1 << x
                break
    for y in range(length):
        for x in range(length):
            if y_bitvector & (1 << y):
                for x2 in range(length):
                    matrix[y][x2] = 0
                break
            if x_bitvector & (1 << x):
                matrix[y][x] = 0
    return matrix


def nullify_matrix2(matrix):
    length = len(matrix[0])
    rows = []
    columns = []
    for y in range(length):
        for x in range(length):
            if matrix[y][x] == 0:
                rows.append(y)
                columns.append(x)
                break
    for row in rows:
        for x in range(length):
            matrix[row][x] = 0
    for column in columns:
        for y in range(length):
            matrix[y][column] = 0
    return matrix


def nullify_matrix3(matrix):
    length = len(matrix[0])
    for y in range(length):
        for x in range(length):
            if matrix[y][x] == 0:
                matrix[0][x] = matrix[y][0] = -1
                break
    for i in range(length):
        if matrix[i][0] == -1:
            for x in range(length):
                if matrix[i][x] != -1:
                    matrix[i][x] = 0
    for i in range(length):
        if matrix[0][i] == -1:
            for y in range(length):
                matrix[y][i] = 0
    return matrix


if __name__ == '__main__':
    n = int(input())
    matrix = [[0] * n for i in range(n)]
    count = 0
    for y in range(n):
        for x in range(n):
            matrix[y][x] = count
            count += 1
    matrix[math.floor(n / 2)][math.floor(n / 2)] = 0

    print(matrix)
    print(nullify_matrix3(matrix))

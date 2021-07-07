import math


def rotate_matrix(matrix):
    length = len(matrix[0])
    rotated = [[i] * length for i in range(length)]
    for y in range(length):
        for x in range(length):
            new_y = x
            new_x = length - 1 - y
            rotated[new_y][new_x] = matrix[y][x]
    return rotated


def rotate_matrix_inplace(matrix):
    length = len(matrix[0])
    last_i = length - 1
    for y in range(math.floor(length / 2)):
        for x in range(math.ceil(length / 2)):
            temp = matrix[last_i - x][y]
            matrix[last_i - x][y] = matrix[last_i - y][last_i - x]
            matrix[last_i - y][last_i - x] = matrix[x][last_i - y]
            matrix[x][last_i - y] = matrix[y][x]
            matrix[y][x] = temp
    return matrix


if __name__ == '__main__':
    n = int(input())
    matrix = [[0] * n for i in range(n)]
    count = 1
    for y in range(n):
        for x in range(n):
            matrix[y][x] = count
            count += 1

    print('Orig:')
    print(matrix)
    print()
    print('Rotated:')
    print(rotate_matrix(matrix))
    print()
    print('Rotated in place:')
    print(rotate_matrix_inplace(matrix))

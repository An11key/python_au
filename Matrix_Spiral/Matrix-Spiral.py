def main_start(N):
    if N == 1:
        print([1])
        return None
    matrix = [[0 for i in range(N)] for j in range(N)]
    index = 1
    border = 0
    while index <= N ** 2:
        index, matrix = move(matrix, border, index, N)
        border += 1
    input_matrix(matrix)


def move(matrix, border, index, N):
    direction = [1, 0, -1, 0]
    col_dir = 3
    raw_dir = 0
    i = j = border
    while True:
        matrix[i][j] += index
        i += direction[col_dir % 4]
        j += direction[raw_dir % 4]
        index += 1
        if matrix[i][j] != 0:
            return index, matrix
        if (i + j - border * 2) % (N - 1 - border * 2) == 0:
            col_dir += 1
            raw_dir += 1
            continue


def input_matrix(matrix):
    for item in matrix:
        print(item)

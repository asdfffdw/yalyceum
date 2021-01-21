def transpose(matrix):
    n = len(matrix)
    matrix += [[matrix[i][j] for i in range(n)] for j in range(len(matrix[0]))]
    del matrix[:n]
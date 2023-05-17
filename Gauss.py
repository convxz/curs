import numpy as np


def eliminate_zeros(matrix):
    def swap_rows(matrix, row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    swap_rows(matrix, i, j)
                    break
    return matrix


def gauss(a: np.zeros) -> np.zeros:
    """
    Функция будет решать уравнения методом Гаусса
    :param a: расширенная матрица
    :return: массив с решениями уравнения в случае, если верны входные данные и не происходит деления на 0, иначе None
    """
    n = len(a)
    x = np.zeros(n)
    a = eliminate_zeros(a)
    for i in range(n):
        if a[i][i] == 0.0:
            return None
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x


a = np.zeros((3, 4))
for i in range(0, 3):
    for j in range(0, 4):
        a[i][j] = int(input())

print(gauss(a))

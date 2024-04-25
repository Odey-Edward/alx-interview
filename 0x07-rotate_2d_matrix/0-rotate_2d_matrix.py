#!/usr/bin/python3
"""2D Matrix Module"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""

    n = len(matrix)

    matrix.reverse()

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

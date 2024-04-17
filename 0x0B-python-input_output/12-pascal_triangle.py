#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Triangle Pascal"""

    mat = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                if i >= 3:
                    row.append(mat[i - 2][j - 1] + mat[i - 2][j])
        mat.append(row)
    return mat

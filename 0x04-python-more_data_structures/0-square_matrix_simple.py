#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = []
    for lst in matrix:
        n_matrix_row = []
        for i in lst:
            x = i ** 2
            n_matrix_row.append(x)
        n_matrix.append(n_matrix_row)

    return n_matrix

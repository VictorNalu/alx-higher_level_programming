#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix == []:
        return []
    new_matrix = []
    for row in matrix:
        new_matrix.append([sub**2 for sub in row])
    return new_matrix

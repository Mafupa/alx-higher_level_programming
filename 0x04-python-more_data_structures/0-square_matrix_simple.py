#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        col = []
        for j in i:
            col.append(j ** 2)
        new.append(col)
    return new

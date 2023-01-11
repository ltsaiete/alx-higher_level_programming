#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    
    newMatrix = []
    for item in matrix:
        newMatrix.append(
            list(map(lambda x: x*x, item))
        )

    return newMatrix

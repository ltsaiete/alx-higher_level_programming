#!/usr/bin/python3

"""
This is a simple module and it has only one function called
matrix_divided
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.

    Args:
        matrix ([[]]): a list of lists of integers or floats
        div (int | float): All elements of the matrix should be divided by div,
        rounded to 2 decimal places

    Returns:
        Returns a new matrix
    """
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []

    for item in matrix:
        if type(item) != list:
            raise TypeError('matrix must be a matrix (list of lists)'
                            ' of integers/floats')

        size = len(matrix[0])
        if len(item) != size:
            raise TypeError('Each row of the matrix must have the same size')
        new_item = []
        for i in item:
            if type(i) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists)'
                                ' of integers/floats')
            new_item.append(round(i / div, 2))
        new_matrix.append(new_item)

    return new_matrix

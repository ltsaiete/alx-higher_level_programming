#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for j in range(len(item)):
            print('{:d}'.format(item[j]), end='')
            if j < len(item) - 1:
                print(end=' ')
        print()

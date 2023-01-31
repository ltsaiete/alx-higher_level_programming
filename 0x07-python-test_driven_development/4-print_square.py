#!/usr/bin/python3
"""
This is the 4-print_square module
It only has one function called print_square
"""


def print_square(size):
    """
    This function  prints a square with the character #
    Args:
        size(int): is the size length of the square

    Returns:
        void
    """
    if type(size) != int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()

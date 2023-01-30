#!/usr/bin/python3
"""
This is a simple module and has only one function call
add_integer
"""


def add_integer(a, b=98):
    """
    This function adds two integer a and b.

    Args:
        a (int | float): First number
        b (int | float): Second number

    Returns:
        Returns an integer: the addition of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)

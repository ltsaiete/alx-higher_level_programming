#!/usr/bin/python3
"""
This is a simple module and it only has
one class called Square
"""


class Square:
    """
     an empty class Square that defines a square
    """

    def __init__(self, size=0):
        """
        This function initializes the class Square

        Args:
            size(int): Size of the square

        Returns:
            void
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
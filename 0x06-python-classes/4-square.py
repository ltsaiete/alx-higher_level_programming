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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        return self.__size * self.__size

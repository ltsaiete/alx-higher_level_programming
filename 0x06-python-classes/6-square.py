#!/usr/bin/python3
"""
This is a simple module and it only has
one class called Square
"""


class Square:
    """
     an empty class Square that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This function initializes the class Square

        Args:
            size(int): Size of the square

        Returns:
            void
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (
            isinstance(value, tuple) and
            list(map(type, value)) == [int, int] and
            list(map(lambda x: x >= 0, value)) == [True, True]
        ):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.__size == 0):
            print()
        for _ in range(self.__size):
            for _ in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#', end='')
            print()

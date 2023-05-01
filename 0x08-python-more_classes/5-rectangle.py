#!/usr/bin/python3
"""
This is a simple module and it only has
one class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    attrs:
        width(int): width of rectangle
        height(int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0

        return self.width * 2 + self.height * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''

        str = ''
        for _ in range(self.height):
            str += '#' * self.width
            str += '\n'

        return str.rstrip('\n')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'

    def __del__(self):
        print('Bye rectangle...')

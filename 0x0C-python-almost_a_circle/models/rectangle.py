#!/usr/bin/python3

"""
This is the rectangle module
It contains the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    This class describes a rectangle
    It inherits the Base class

    Args:
        Base (class): Parent class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        for k, v in locals().items():
            if v in [width, height, x, y]:
                if type(v) != int:
                    raise TypeError(f'{k} must be an integer')

            if v in [width, height]:
                if v <= 0:
                    raise ValueError(f'{k} must be > 0')
            if v in [x, y]:
                if v < 0:
                    raise ValueError(f'{k} must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')

        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')

        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if type(x) != int:
            raise TypeError('x must be an integer')

        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if type(y) != int:
            raise TypeError('y must be an integer')

        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        print('\n' * self.__y, end='')

        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        str = f'[Rectangle] ({self.id}) {self.__x}/'
        str += f'{self.__y} - {self.__width}/{self.__height}'
        return str

    def update(self, *args, **kwargs):
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.set_width(args[i])
                elif i == 2:
                    self.set_height(args[i])
                elif i == 3:
                    self.set_x(args[i])
                elif i == 4:
                    self.set_y(args[i])
        elif kwargs is not None:

            for k, v in kwargs.items():
                if k == 'width':
                    self.set_width(v)
                elif k == 'height':
                    self.set_height(v)
                elif k == 'x':
                    self.set_x(v)
                elif k == 'y':
                    self.set_y(v)
                elif k == 'id':
                    self.id = v

    def to_dictionary(self):
        dict = {
            'id': self.id,
            'width': self.get_width(),
            'height': self.get_height(),
            'x': self.get_x(),
            'y': self.get_y()
        }
        return dict


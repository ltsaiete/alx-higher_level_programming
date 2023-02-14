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
        """
        Creates an instance of Rectangle

        Args:
            width (int): width
            height (int): height
            x (int, optional): initial position. Defaults to 0.
            y (int, optional): position. Defaults to 0.
            id (int, optional): Rectangle id. Defaults to None.

        Raises:
            TypeError: att must be integers
            ValueError: Validates the args values
            ValueError: _description_
        """
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
        """get the width

        Returns:
            int: width
        """
        return self.__width

    def set_width(self, width):
        """Set the width

        Args:
            width (int): new width

        Raises:
            TypeError: Validates type
            ValueError: Validates value
        """
        if type(width) != int:
            raise TypeError('width must be an integer')

        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    def get_height(self):
        """get the height

        Returns:
            int: height
        """
        return self.__height

    def set_height(self, height):
        """Set the height

        Args:
            height (int): new height

        Raises:
            TypeError: Validates type
            ValueError: Validates value
        """
        if type(height) != int:
            raise TypeError('height must be an integer')

        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    def get_x(self):
        """get the x

        Returns:
            int: x
        """
        return self.__x

    def set_x(self, x):
        """Set the x

        Args:
            x (int): new x

        Raises:
            TypeError: Validates type
            ValueError: Validates value
        """
        if type(x) != int:
            raise TypeError('x must be an integer')

        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    def get_y(self):
        """get the y

        Returns:
            int: y
        """
        return self.__y

    def set_y(self, y):
        """Set the y

        Args:
            y (int): new y

        Raises:
            TypeError: Validates type
            ValueError: Validates value
        """
        if type(y) != int:
            raise TypeError('y must be an integer')

        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """calculates area of rectangle

        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle
        using #s
        """
        print('\n' * self.__y, end='')

        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """
         returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

        Returns:
            _type_: _description_
        """
        str = f'[Rectangle] ({self.id}) {self.__x}/'
        str += f'{self.__y} - {self.__width}/{self.__height}'
        return str

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute:
        """
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
        """
        returns the dictionary representation of a Rectangle

        Returns:
            dict: dictionary representation of a Rectangle
        """
        dict = {
            'id': self.id,
            'width': self.get_width(),
            'height': self.get_height(),
            'x': self.get_x(),
            'y': self.get_y()
        }
        return dict

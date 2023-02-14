#!/usr/bin/python3
"""
This is the module square
It is a simple module and only contains the class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the class Square
    It inherits from Rectangle

    Args:
        Rectangle (class): Class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Creates an instance of Square

        Args:
            size (int): size
            x (int, optional): initial position. Defaults to 0.
            y (int, optional): position. Defaults to 0.
            id (int, optional): Square id. Defaults to None.

        Raises:
            TypeError: att must be integers
            ValueError: Validates the args values
            ValueError: _description_
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
         returns [Rectangle] (<id>) <x>/<y> - <size>

        Returns:
            _type_: _description_
        """
        str = f'[Square] ({self.id}) {self.get_x()}/'
        str += f'{self.get_y()} - {self.get_width()}'
        return str

    @property
    def get_size(self):
        """get the size

        Returns:
            int: size
        """
        return self.get_width()

    @set_size.setter
    def set_size(self, size):
        """Set the size

        Args:
            size (int): new size
        """
        self.set_width(size)
        self.set_height(size)

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
                    self.set_height(args[i])
                elif i == 2:
                    self.set_x(args[i])
                elif i == 3:
                    self.set_y(args[i])
        elif kwargs is not None:

            for k, v in kwargs.items():
                if k == 'size':
                    self.set_width(v)
                    self.set_height(v)
                elif k == 'x':
                    self.set_x(v)
                elif k == 'y':
                    self.set_y(v)
                elif k == 'id':
                    self.id = v

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square

        Returns:
            dict: dictionary representation of a Square
        """
        dict = {
            'id': self.id,
            'size': self.get_size(),
            'x': self.get_x(),
            'y': self.get_y()
        }
        return dict

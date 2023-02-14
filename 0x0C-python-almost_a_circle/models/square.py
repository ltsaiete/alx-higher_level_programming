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
        str = f'[Square] ({self.id}) {self.x}/'
        str += f'{self.y} - {self.width}'
        return str

    @property
    def size(self):
        """get the size

        Returns:
            int: size
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set the size

        Args:
            size (int): new size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute:
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs is not None:

            for k, v in kwargs.items():
                if k == 'size':
                    self.width = v
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v
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
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return dict

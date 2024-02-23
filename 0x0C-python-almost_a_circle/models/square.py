#!/usr/bin/python3

"""
This module imports the Rectangle model
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from the Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instance of the Rectangle-Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation
        """
        return "[Square] ({}){:d}/{:d} - {:d}".format(self.id, self.x,
                                                      self.y, self.size)

    @property
    def size(self):
        """
        return width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets new value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Take arguments
        """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']

            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attr[i], args[i])
            else:
                for key, value in kwargs.items():
                    if key == 'size':
                        setattr(self, 'width', value)
                        setattr(self, 'height', value)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Dictionary representation of Rectangle
        """
        d1 = self.__dict__
        d2 = {}
        d2['id'] = d1['id']
        d2['size'] = d1['_Rectangle__width']
        d2['x'] = d1['_Rectangle__x']
        d2['y'] = d1['_Rectangle__y']

        return d2

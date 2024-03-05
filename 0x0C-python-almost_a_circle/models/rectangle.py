#!/usr/bin/python3

""" Define the class rectangle """


from models.base import Base


class Rectangle(Base):
    """The class inherits from the class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """The class instantiation """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the value of the width """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for the width """
        self.__width = value

    @property
    def height(self):
        """Returns the value of the height """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for the height """
        self.__height = value

    @property
    def x(self):
        """Returns the value of the x  """
        return self.__y

    @x.setter
    def x(self, value):
        """Property setter for the x """
        self.__x = value

    @property
    def y(self):
        """Returns the value of the y """
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for the y """
        self.__y = value

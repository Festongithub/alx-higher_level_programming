#!/usr/bin/python3

"""BaseGeometrty
"""

class BaseGeometry:
    """Contains area(), integer_validator()
    """

    def area():
        """Function not implemented """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate"""

        if type != int:
            raise TypeError(name  +  "must be an integer")

        if value <= 0:
            raise ValueError(name +  "must be greater than 0")

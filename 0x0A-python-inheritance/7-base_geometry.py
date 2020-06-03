#!/usr/bin/python3
"""This module holds a function with
Geometry module
    """


class BaseGeometry:
    """Integer validator
    """

    def area(self):
        """Public instance method that raise an exception

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method, that check value

        Arguments:
            name {[str]} -- instance name
            value {[int]} -- instance value

        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

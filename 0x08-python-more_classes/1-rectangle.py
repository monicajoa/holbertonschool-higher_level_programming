#!/usr/bin/python3
"""This module hold a class
that defines a rectangle
"""


class Rectangle:
    """class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize the object

        Keyword Arguments:
            width {int} -- rectangle width (default: {0})
            height {int} -- rectangle height (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """width setter

        Arguments:
            value {[int]} -- rectangle width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """height setter

        Arguments:
            value {[int]} -- rectangle height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

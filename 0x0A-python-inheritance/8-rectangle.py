#!/usr/bin/python3
"""This module holds a class Rectangle
    """
BaseGeo = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeo):
    """class rectangle that inherits from BaseGeometry

    Arguments:
        BaseGeo {[class]} -- Baseclass
    """

    def __init__(self, width, height):
        """Constructor or initializer

        Arguments:
            width {[int]} -- width of the rectangle
            height {[int]} -- height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

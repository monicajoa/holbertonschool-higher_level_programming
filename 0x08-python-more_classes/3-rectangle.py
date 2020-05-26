#!/usr/bin/python3
"""This module hold a class
that defines a rectangle
"""


class Rectangle:
    """class that defines a rectangle (string representation)
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

    def area(self):
        """Returns the rectangle area
        Returns:
            [int] -- Rectangle area
        """
        return (self.width * self.height)

    def perimeter(self):
        """Returns the rectangle perimeter
        Returns:
            [int] -- Rectangle perimeter
        """
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return ((self.width + self.height) * 2)

    def __str__(self):
        str_temp = ""
        if self.width is 0 or self.height is 0:
            return (str_temp)
        else:
            for i in range(self.height):
                for j in range(self.width):
                    str_temp += "#"
                str_temp += "\n"
            return (str_temp[:-1])

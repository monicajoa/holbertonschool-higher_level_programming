#!/usr/bin/python3
"""This module holds a function
    with class Rectangle
    """
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base

    Arguments:
        Base {[class]} -- class that initilize an
        object with a specific id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method

        Arguments:
            width {[int]} -- width of rectangle
            height {[int]} -- height of rectangle

        Keyword Arguments:
            x {int} -- x value (default: {0})
            y {int} -- y value (default: {0})
            id {[int]} -- unique number that
            identify the object (default: {None})
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """method with representation as a string

        Returns:
            [str] -- string of the rectangle
        """
        str_id = str(self.id)
        str_width = str(self.width)
        str_height = str(self.height)
        str_x = str(self.x)
        str_y = str(self.y)
        str_new = "[Rectangle] (" + str_id + ") " + str_x + "/" + str_y + " - "
        str_new = str_new + str_width + "/" + str_height
        return str_new

    @property
    def width(self):
        """width getter

        Returns:
            [int] -- width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Arguments:
            value {[obj]} -- value to assign

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            [int] -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Arguments:
            value {[obj]} -- value to assign

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter

        Returns:
            [int] -- x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter

        Arguments:
            value {[obj]} -- value to assign

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter

        Returns:
            [int] -- y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter

        Arguments:
            value {[obj]} -- value to assign

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """method with the area of the rectangle

        Returns:
            [int] -- area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """print the rectangle with the '#'
        """
        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """method that update an instance
        """
        if args:
            index = 0
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """public method that gives a instance as a dictionary

        Returns:
            [dic] -- instance representation
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }

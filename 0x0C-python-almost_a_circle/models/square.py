#!/usr/bin/python3
"""This module holds a function
    with class Square
    """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle

    Arguments:
        Rectangle {[class]} -- Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor method

        Arguments:
            size {[int]} -- size of the square

        Keyword Arguments:
            x {int} -- x value (default: {0})
            y {int} -- y value (default: {0})
            id {[int]} -- unique number that
            identify the object (default: {None})
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter

        Returns:
            [int] -- size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter

        Arguments:
            value {[obj]} -- value to assign
        """
        self.width = value
        self.height = value

    def __str__(self):
        """"method with representation as a string

        Returns:
            [str] -- string of the square
        """
        str_id = str(self.id)
        str_height = str(self.height)
        str_x = str(self.x)
        str_y = str(self.y)
        str_new = "[Square] (" + str_id + ") " + str_x + "/" + str_y + " - "
        str_new = str_new + str_height
        return str_new

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
                    self.height = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
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
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y,
        }

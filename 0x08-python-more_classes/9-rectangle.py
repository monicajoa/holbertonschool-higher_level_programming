#!/usr/bin/python3
"""This module hold a class
that defines a rectangle
"""


class Rectangle:
    """class that defines a rectangle (a square is a rectangle)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the object

        Keyword Arguments:
            width {int} -- rectangle width (default: {0})
            height {int} -- rectangle height (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """rectangle as a string with # character

        Returns:
            [list] -- representation  of the rectangle as a str
        """
        str_temp = ""
        if self.width is 0 or self.height is 0:
            return (str_temp)
        else:
            for i in range(self.height):
                for j in range(self.width):
                    str_temp += str(self.print_symbol)
                str_temp += "\n"
            return (str_temp[:-1])

    def __repr__(self):
        """representation of rectangle as an instance

        Returns:
            [str] -- str as an instance
        """
        a = str(self.width)
        b = str(self.height)
        return ("Rectangle(" + a + ", " + b + ")")

    def __del__(self):
        """deletes an object or instance
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare two rectangles by area

        Arguments:
            rect_1 {[Rectangle]} -- first rectangle to compare
            rect_2 {[Rectangle]} -- second rectangle to compare

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_2 must be an instance of Rectangle

        Returns:
            [Rectangle] -- biggest rectangle or rect_1
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() == rect_2.area():
                return (rect_1)
            elif rect_1.area() > rect_2.area():
                return (rect_1)
            else:
                return (rect_2)

    @classmethod
    def square(cls, size=0):
        """new square as a rectangle

        Keyword Arguments:
            size {int} -- size of the square (default: {0})

        Returns:
            [Rectangle] -- instance of square
        """
        return (cls(size, size))

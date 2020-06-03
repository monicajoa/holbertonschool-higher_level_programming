#!/usr/bin/python3
"""This module holds a class MyInt
    """


class MyInt(int):
    """new class MyInt has == and != operators inverted

    Arguments:
        int {[class]} -- Parent class
    """

    def __eq__(self, number):
        """equal method

        Arguments:
            number {[int]} -- integer to compare

        Returns:
            [bool] -- inverted operator
        """
        return int(self) != int(number)

    def __ne__(self, number):
        """diferent method

        Arguments:
            number {[int]} -- integer to compare

        Returns:
            [bool] -- inverted operator
        """
        return int(self) == int(number)

#!/usr/bin/python3
"""This module holds a function
    with number of lines of a text
    """


def number_of_lines(filename=""):
    """ function that returns the number
    of lines of a text file

    Keyword Arguments:
        filename {str} -- string to read and count the lines (default: {""})

    Returns:
        [str] -- number of lines of a text file
    """
    with open(filename) as file:
        n_lines = 0
        for line in file:
            n_lines += 1
        return n_lines

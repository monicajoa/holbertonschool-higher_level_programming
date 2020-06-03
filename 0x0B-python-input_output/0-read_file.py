#!/usr/bin/python3
"""This module holds a function
    that reads a text file
    """


def read_file(filename=""):
    """function that reads a text file
    and prints it to stdout

    Keyword Arguments:
        filename {str} -- string to read and print (default: {""})
    """
    with open(filename) as file:
        for line in file:
            print(line, end="")

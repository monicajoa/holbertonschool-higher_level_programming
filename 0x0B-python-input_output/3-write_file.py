#!/usr/bin/python3
"""This module holds a function
    that write to a file
    """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    and returns the number of characters written

    Keyword Arguments:
        filename {str} -- string to read and return
        number characters (default: {""})
        text {str} -- text to write in the file (default: {""})

    Returns:
        [int] -- number of characters written
    """
    with open(filename, "w") as file:
        return file.write(text)

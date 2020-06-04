#!/usr/bin/python3
"""This module holds a function
    that append to a file
    """


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    and returns the number of characters added

    Keyword Arguments:
        filename {str} -- string to read and return
        number characters add  (default: {""})
        text {str} -- text to append in the text (default: {""})

    Returns:
        [int] -- number of characters added
    """
    with open(filename, "a") as file:
        return file.write(text)

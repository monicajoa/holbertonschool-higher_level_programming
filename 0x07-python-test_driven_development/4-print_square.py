#!/usr/bin/python3
"""
This module hold a function that prints a square with the character #.
"""


def print_square(size):
    """
    This function prints square by the size
    Paramethers:
        size: length of the square
    Errors:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    Returns:
        Nothing
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if (type(size) is float and size < 0):
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print('#', end="")
        print()

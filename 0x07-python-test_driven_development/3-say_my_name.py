#!/usr/bin/python3
"""
This module hold a function that prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints the first and the last name
    Paramethers:
        first_name: The first name
        last_name: The last name
    Errors:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    Returns:
        Nothing
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

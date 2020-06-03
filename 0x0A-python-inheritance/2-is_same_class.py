#!/usr/bin/python3
"""This module holds a function that check if the object
    is exactly an instance of the specified class
    """


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Arguments:
        obj {[object]} -- object to check
        a_class {[class]} -- specified class

    Returns:
        [bool] -- if is an instance return true otherwise false
    """
    return type(obj) == a_class

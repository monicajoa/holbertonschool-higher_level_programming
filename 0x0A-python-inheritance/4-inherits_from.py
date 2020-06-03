#!/usr/bin/python3
"""This module holds a function that
    check if is only sub class from another class
    """


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class that 
    inherited (directly or indirectly) from the specified class ; otherwise False.

    Arguments:
        obj {[object]} -- object to check
        a_class {[class]} -- specified class

    Returns:
        [bool] -- if is an subclass return true otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

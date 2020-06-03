#!/usr/bin/python3
"""This module holds a function that
    check if is Same class or inherit from
    """


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    Arguments:
        obj {[object]} -- object to check
        a_class {[class]} -- specified class

    Returns:
        [bool] -- if is an instance or inherited return true otherwise false
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
    """This module holds a function that returns the list 
    of available attributes and methods of an object
    """


def lookup(obj):
    """function that returns the list 
    of available attributes and methods of an object

    Arguments:
        obj {[object]} -- object to check

    Returns:
        [list] -- available attributes and methods of an object
    """
    return dir(obj)

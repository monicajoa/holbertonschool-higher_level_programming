#!/usr/bin/python3
"""This module holds a function
    whit a class to JSON
    """


def class_to_json(obj):
    """function that returns the dictionary description with simple
    data structure for JSON serialization of an object

    Arguments:
        obj {[data structure]} -- instance of a Class

    Returns:
        [dict] -- dictionary with simple data structure
        (list, dictionary, string, integer and boolean
    """
    return obj.__dict__

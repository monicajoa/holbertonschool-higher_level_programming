#!/usr/bin/python3
"""This module holds a function
    JSON representation string
    """
import json


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)

    Arguments:
        my_obj {[str]} -- object to convert in json representation

    Returns:
        [type] -- JSON representation of an object (string)
    """
    return json.dumps(my_obj, sort_keys=True)

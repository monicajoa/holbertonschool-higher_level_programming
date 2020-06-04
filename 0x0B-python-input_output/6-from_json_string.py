#!/usr/bin/python3
"""This module holds a function
    From JSON string to Object
    """
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string

    Arguments:
        my_str {[str]} -- string to convert to object

    Returns:
        [object] -- (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)

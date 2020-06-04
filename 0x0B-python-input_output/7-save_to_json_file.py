#!/usr/bin/python3
"""This module holds a function
    that save Object to a file
    """
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a
    text file, using a JSON representation

    Arguments:
        my_obj {[object]} -- object to transform in json string
        filename {[type]} -- file that save json string
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

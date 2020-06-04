#!/usr/bin/python3
"""This module holds a function
    that create object from a JSON file
    """
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”

    Arguments:
        filename {[srt]} -- name of the json file

    Returns:
        [str] -- new object of json file
    """
    with open(filename, "r") as file:
        ob_new = json.load(file)
        return ob_new

#!/usr/bin/python3
"""This module holds a function
    with the base class
    """
import json


class Base:
    """class that initilize an object with a
    specific id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method

        Keyword Arguments:
            id {[int]} -- unique number that
            identify the object (default: {None})
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to json string

        Arguments:
            list_dictionaries {[list]} -- list of dictionaries

        Returns:
            [str] -- json string representation of list_dictionaries
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string
        representation of list_objs to a file

        Arguments:
            list_objs {[list]} -- list of instances who inherits of Base
        """
        if list_objs:
            n_list = [items.to_dictionary() for items in list_objs]
        else:
            n_list = "[]"
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as work_file:
            work_file.write(Base.to_json_string(n_list))

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of the JSON
        string representation json_string

        Arguments:
            json_string {[str]} -- string representing a list of dictionaries

        Returns:
            [list] --  list of the JSON string representation
        """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance
        with all attributes already set

        Returns:
            [obj] -- instance with all attributes
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 3)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method with a file to instances

        Returns:
            [list] -- list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as work_file:
                return [
                    cls.create(**dic_new)
                    for dic_new in cls.from_json_string(work_file.read())
                ]
        except:
            return []

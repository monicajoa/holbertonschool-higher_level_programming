#!/usr/bin/python3
"""This module holds a function
    a class student to JSON with filter
    """


class Student:
    """class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Constructor - public instance attributes

        Arguments:
            first_name {[str]} -- first name's student
            last_name {[str]} -- last name's student
            age {[int]} -- age's student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to convert an object to dict

        Keyword Arguments:
            attrs {[list]} -- attrs to return in the dict (default: {None})

        Returns:
            [dict] -- dictionary with attrs in the list
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dic = {}
            for attr_items in attrs:
                if attr_items in self.__dict__:
                    new_dic.update({attr_items: self.__dict__[attr_items]})
            return new_dic

    def reload_from_json(self, json):
        """ method that replaces all
        attributes of the student instance
        """
        for i in json:
            self.__dict__.update({i: json[i]})

#!/usr/bin/python3
"""This module holds a function
    a class student to JSON
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

    def to_json(self):
        """ function that retrieves a dictionary
        representation of a Student instance

        Returns:
            [dict] -- dictionary representation of a Student
        """
        return self.__dict__

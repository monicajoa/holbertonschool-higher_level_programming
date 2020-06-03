#!/usr/bin/python3
"""This module holds a class MyList
    that inherits from list
    """


class MyList(list):
    """Class MyList that inherits from list
    """

    def print_sorted(self):
        """Prints the new list, but sorted (ascending)
        """
        print(sorted(self))

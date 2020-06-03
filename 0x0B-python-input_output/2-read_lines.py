#!/usr/bin/python3
"""This module holds a function that
    reads n lines of a text file
    """


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a
    text file and prints it to stdout:

    Keyword Arguments:
        filename {str} -- string to read and print n lines (default: {""})
        nb_lines {int} -- number of lines to print (default: {0})
    """
    with open(filename) as file:
        n_lines = 0
        for line in file:
            n_lines += 1
        if nb_lines <= 0 or nb_lines >= n_lines:
            file.seek(0)
            for line in file:
                print(line, end="")
        else:
            file.seek(0)
            for line in range(nb_lines):
                print(file.readline(), end="")

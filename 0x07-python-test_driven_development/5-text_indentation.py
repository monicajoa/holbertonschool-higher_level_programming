#!/usr/bin/python3
"""This module hold a function that prints a indented text
"""


def text_indentation(text):
    """This function prints a text with 2 new lines
    after each of these characters: ., ? and :

    Arguments:
        text {[str]} -- string to check

    Raises:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in range(len(text)):
        m = text[x - 1]
        n = text[x]
        if not (n == ' ' and (m == '.' or m == '?' or m == ':' or m == ' ')):
            if n == '.' or n == '?' or n == ':':
                print("{}\n".format(n))
            else:
                print(n, end="")

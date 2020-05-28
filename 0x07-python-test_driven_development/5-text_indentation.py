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
    for i in range(len(text)):
        m = text[i - 1]
        if not (text[i] == ' ' and (m == '.' or m == '?' or m == ':')):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print("{}\n".format(text[i]))
            else:
                print(text[i], end="")

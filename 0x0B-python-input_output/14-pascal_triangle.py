#!/usr/bin/python3
"""This module holds a function
    with pascal's Triangle
    """


def pascal_triangle(n):
    """function that returns a list of lists of integers
    representing the Pascal’s triangle of n

    Arguments:
        n {[int]} -- size of pascal's triangle

    Returns:
        [list] -- lists of integers representing the triangle
    """
    n_list = []
    if n <= 0:
        return n_list
    else:
        for i in range(n):
            sub_list = []
            sub_list.append(1)
            for j in range(1, i):
                sub_list.append(n_list[i - 1][j - 1] + n_list[i - 1][j])
            if i != 0:
                sub_list.append(1)
            n_list.append(sub_list)
        return n_list

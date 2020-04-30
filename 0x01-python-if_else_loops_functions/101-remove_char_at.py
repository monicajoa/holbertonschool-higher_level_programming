#!/usr/bin/python3
def remove_char_at(str, n):
    strnew = ""
    j = 0
    for i in str:
        if j != n:
            strnew += i
        j += 1
    return (strnew)

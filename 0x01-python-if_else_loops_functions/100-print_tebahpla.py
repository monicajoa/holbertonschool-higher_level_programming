#!/usr/bin/python3
str2 = ""
for i in range(122, 96, -1):
    if i % 2 == 0:
        str2 = str2 + chr(i)
    else:
        str2 = str2 + chr(i - 32)
print("{:s}".format(str2), end='')

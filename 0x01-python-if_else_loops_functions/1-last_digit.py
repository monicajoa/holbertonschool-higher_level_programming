#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ld = number % 10
else:
    ld = number % -10
str1 = "Last digit of"
if ld > 5:
    print("{} {} is {} and is greater than 5".format(str1, number, ld))
elif ld == 0:
    print("{} {} is {} and is 0".format(str1, number, ld))
else:
    str_tem = "and is less than 6 and not 0"
    print("{} {} is {} {}".format(str1, number, ld, str_tem))

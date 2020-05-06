#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for x in matrix:
            for item in range(0, len(x)):
                if item < len(x) - 1:
                    print("{:d}".format(x[item]), end=" ")
                else:
                    print("{:d}".format(x[item]))

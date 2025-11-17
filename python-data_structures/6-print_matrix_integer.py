#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row[:-1]:
            print("{:d}".format(num), end=" ")
        if row:
            print("{:d}".format(row[-1]))
        else:
            print("")


# CLEAN VERSION !
# def print_matrix_integer(matrix=[[]]):
#    for row in matrix:
#        print(" ".join("{:d}".format(num) for num in row))

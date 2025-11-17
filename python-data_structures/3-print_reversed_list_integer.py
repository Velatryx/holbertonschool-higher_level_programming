#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    return my_list


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5]
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))

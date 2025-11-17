#!/usr/bin/python3
#
#
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 10]
    print_list_integer(my_list)
#
#
# custom_list = ['v', 'e', 'l', 'a', 't', 'r', 'y', 'x']
#
#
# def print_list_integer(my_list=[]):
#    return str.format(my_list)
# if __name__ == "__main__":
#    for i in range(0, len(custom_list)):
#        print("{}".format(f"{custom_list[i]}", end="\n"))

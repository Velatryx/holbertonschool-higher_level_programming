#!/usr/bin/python3


def common_elements(set_1, set_2):
    return set_1 & set_2


# def common_elements(set_1, set_2):
#    set_0 = set()
#    for x in set_1:
#        if x in set_2:
#           set_0.add(x)
#    return set_0
#
#
#
if __name__ == "__main__":
    set_1 = {1, 2, 3, 'Holberton', 'School'}
    set_2 = {2, 4, 5, 'Holberton', 'Hello'}
    print(common_elements(set_1, set_2))

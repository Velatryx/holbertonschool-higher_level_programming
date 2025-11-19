#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    return set_1 - set_2


if __name__ == "__main__":
    set_1 = {1, 2, 4, 'Holberton'}
    set_2 = {3, 4, 5, 'Hello'}
    print(only_diff_elements(set_1, set_2))

#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4]
    print(new_in_list(my_list, 1, 7))

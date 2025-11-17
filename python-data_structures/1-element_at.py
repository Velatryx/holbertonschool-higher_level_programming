#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None
    return my_list[idx]


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4]
    idx = 5
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

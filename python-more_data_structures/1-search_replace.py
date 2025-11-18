#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 2, 2, 2, 3, 1, 90]
    print(search_replace(my_list, 2, 10))

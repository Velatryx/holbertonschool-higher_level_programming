#!/usr/bin/python3


def uniq_add(my_list=[]):
    s = []
    return sum(x for x in my_list if x not in s and not s.append(x))

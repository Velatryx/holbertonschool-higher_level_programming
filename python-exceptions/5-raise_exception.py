#!/usr/bin/python3


def raise_exception():
    try:
        print("1" + 1)
    except TypeError:
        print("Exception raised")


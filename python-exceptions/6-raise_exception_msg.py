#!/usr/bin/python3


def raise_exception_msg(message=""):
    try:
        print("1" + 1)
    except TypeError:
        print(message)


if __name__ == "__main__":
    message = "Type Error Occured. Please fix your code."
    print(raise_exception_msg(message))

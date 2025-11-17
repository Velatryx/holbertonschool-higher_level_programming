#!/usr/bin/python3


def no_c(my_string):
    string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            string += char
    return string


if __name__ == "__main__":
    hello = "hello, C!"
    print(no_c(hello))

#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print("{}".format("0 arguments."))
    elif num == 1:
        print("{}".format("1 argument:"))
        print("{}".format(f"1: {argv[1]}"))
    else:
        print("{}".format(f"{num} arguments."))
        for i in (1, num):
            print("{}".format(f"{i}: {argv[i]}", end="\n"))

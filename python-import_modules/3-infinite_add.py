#!/usr/bin/python3
from math import *
from sys import argv
if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print("{}".format("0"))
    else:
        sum = 0
        for i in range(1, num + 1):
            sum += int(argv[i])
        print("{}".format(f"{sum}"))

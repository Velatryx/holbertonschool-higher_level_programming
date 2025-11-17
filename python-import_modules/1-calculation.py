#!/usr/bin/python3
from calculator_1 import add  ##Normally use import *, but it is forbidden for this task.
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div
a = 10
b = 5
if __name__ == "__main__":
    print("{}".format(f"{a} + {b} = {add(a, b)}"))
    print("{}".format(f"{a} - {b} = {sub(a, b)}"))
    print("{}".format(f"{a} * {b} = {mul(a, b)}"))
    print("{}".format(f"{a} / {b} = {div(a, b)}"))

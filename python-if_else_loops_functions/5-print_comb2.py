#!/usr/bin/python3
for n in range(100):
    print("{:02d}".format(n) + (", " if n < 99 else "\n"), end="")

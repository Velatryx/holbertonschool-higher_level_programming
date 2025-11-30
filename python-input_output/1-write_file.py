#!/usr/bin/python3
"""Defines a function that writes to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the number of chars."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

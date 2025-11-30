#!/usr/bin/python3
"""Defines a function that appends text to a file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 file and return chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

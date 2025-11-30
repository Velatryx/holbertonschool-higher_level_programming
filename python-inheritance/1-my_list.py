#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that can print a sorted version of itself."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

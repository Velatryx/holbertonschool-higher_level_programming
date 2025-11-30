#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""
    

class MyList(list):
    """A custom list class that can print a sorted version of itself."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))

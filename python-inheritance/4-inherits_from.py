#!/usr/bin/python3
"""Defines a function that checks class inheritance."""
    

def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class
    (directly or indirectly); otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

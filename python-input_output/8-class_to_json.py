#!/usr/bin/python3
"""Define function that returns the dictionary description of an object"""


def class_to_json(obj):
    """Return dictionary description for JSON serialization of an obj"""
    return obj.__dict__

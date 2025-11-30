#!/usr/bin/python3
"""Defines a function that saves an object to a text file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

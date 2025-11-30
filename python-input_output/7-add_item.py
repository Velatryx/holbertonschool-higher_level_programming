#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""

import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# Load existing list if file exists, otherwise start with empty list
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all command-line arguments except the script name
my_list.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(my_list, filename)

#!/usr/bin/python3
"""Convert CSV data to JSON file."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and save as data.json.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True on success, False on failure.
    """
    try:
        data_list = []

        # Read CSV file
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        # Write JSON file
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except Exception:
        return False

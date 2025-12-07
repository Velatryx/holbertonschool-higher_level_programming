#!/usr/bin/env python3
"""
Generates invitation files using a template and a list of attendee dictionaries.
"""

import os


def generate_invitations(template, attendees):
    """
    Generates invitation text files by replacing placeholders in a template.

    Args:
        template (str): The template string containing placeholders.
        attendees (list): A list of dictionaries with attendee information.
    """

    # -------- Type Checks --------
    if not isinstance(template, str):
        print("Invalid input: template should be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Invalid input: attendees should be a list of dictionaries.")
        return

    # -------- Empty Checks --------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -------- Process Each Attendee --------
    for index, attendee in enumerate(attendees, start=1):
        filled = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            filled = filled.replace("{" + key + "}", str(value))

        # Write output file
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as f:
                f.write(filled)
        except Exception:
            print(f"Error writing to {filename}")
            return

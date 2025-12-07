#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter.
The letter is sent in the variable q.
Handles JSON response and prints result or proper messages.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    # If no argument provided → q = ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {"q": q}

    try:
        r = requests.post(url, data=data)
        json_data = r.json()  # May raise ValueError if invalid JSON

        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

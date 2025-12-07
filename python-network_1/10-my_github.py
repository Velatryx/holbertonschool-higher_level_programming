#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication to display the user ID.
The second argument must be a personal access token.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, token))

    try:
        json_data = r.json()
        print(json_data.get("id"))
    except ValueError:
        print("None")

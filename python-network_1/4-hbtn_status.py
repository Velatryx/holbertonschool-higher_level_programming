#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
and displays the body in a specific format.
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")

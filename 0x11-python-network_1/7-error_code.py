#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a requesto to the URL
and displays the body response
"""


from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)

    # Check the response status code and print appropriate messages
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code:", response.status_code)

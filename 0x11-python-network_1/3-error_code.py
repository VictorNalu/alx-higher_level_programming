#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    try:
        # Send a request to the URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the body of the response
            html = response.read().decode("utf-8")
            # Display the body of the response
            print(html)

    except urllib.error.HTTPError as e:
        # If HTTPError occurs, print the error code
        print("Error code:", e.code)

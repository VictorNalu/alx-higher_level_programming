#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
"""

import sys
import requests

if __name__ == "__main__":
    # Get the URL from command line argument
    url = sys.argv[1]

    # Send a request to the URL
    response = requests.get(url)

    # Display the value of the X-Request-Id variable
    print(response.headers.get("X-Request-Id"))

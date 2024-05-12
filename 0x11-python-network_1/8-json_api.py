#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main":

    # Set default value for q if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send a POST request to the URL with the letter as a parameter
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        # Parse the JSON response
        data = response.json()

        if data:
            # Display id and name if JSON is properly formatted and not empty
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            # Display "No result" if JSON is empty
            print("No result")
    except ValueError:
        # Display "Not a valid JSON" if JSON is invalid
        print("Not a valid JSON")

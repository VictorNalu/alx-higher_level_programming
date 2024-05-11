#!/bin/bash
# A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o response.txt -w "%{http_code}" "$1" >/dev/null

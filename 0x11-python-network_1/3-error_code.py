#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

try:
    # Get the URL from the command line arguments
    url = sys.argv[1]

    # Send the request to the URL
    response = urllib.request.urlopen(url)

    # Decode the response body in utf-8
    body = response.read().decode('utf-8')

    # Print the response body
    print(body)

except urllib.error.HTTPError as e:
    # Print the error code
    print(f"Error code: {e.code}")

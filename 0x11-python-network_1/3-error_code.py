#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        # Get the URL from the command line arguments
        url = sys.argv[1]

    # Send the request to the URL
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)

except urllib.error.HTTPError as e:
    # Print the error code
    print("Error code:{}".format(e.code))

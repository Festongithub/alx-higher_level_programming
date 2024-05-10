#!/usr/bin/python3

"""
 Python script that fetches https://alx-intranet.hbtn.io/status
 """

import requests

if __name__ == "__main__":
    r = "https://alx-intranet.hbtn.io/status"
    response = requests.get(r)
    content = response.text
    print("Body response:")
    print("-type: {}".format(type(content)))
    print("-content: {}".format(content))

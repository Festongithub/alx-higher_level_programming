#!/usr/bin/python3

"""
Saving text object to text file in JSON format
"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)

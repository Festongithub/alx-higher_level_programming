#!/usr/bin/python3

"""
Saving text object to text file in JSON format
"""

import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dumps(my_obj, f)

#!/usr/bin/python3

"""
A module that jsonify texts
"""

import json


def to_json_string(my_obj):
    """
    Returns json string of an object
    """
    return json.dumps(my_obj)

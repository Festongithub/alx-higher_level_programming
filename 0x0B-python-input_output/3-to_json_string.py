#!/usr/bin/python3

import json
"""
A module that jsonify texts
"""


def to_json_string(my_obj):
    """
    Returns json string of an object
    """
    return json.dumps(my_obj)

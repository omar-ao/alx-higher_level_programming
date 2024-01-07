#!/usr/bin/python3
"""This is the ``3-to_json_string`` module
It contains one function, to_json_string
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    """
    return json.dumps(my_obj)

#!/usr/bin/python3
"""This is the ``8-class_to_json`` module
It contains one function, class_to_json
"""


import json


def class_to_json(obj):
    """
    Returns the dictionary description of the object ``obj``
    """
    return json.dumps(obj.__dict__)

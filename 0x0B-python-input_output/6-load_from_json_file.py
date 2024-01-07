#!/usr/bin/python3
"""This is the ``load_from_json_file`` module
It contains one function, load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file"
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

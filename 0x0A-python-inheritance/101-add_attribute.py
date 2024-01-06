#!/usr/bin/python3
"""
This is the ``101-add_attribute`` module
It defines one function add_attribute
"""


def add_attribute(obj, name, value):
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__setattr__(name, value)

#!/usr/bin/python3
"""The ``2-is_same_class`` module.
This module  contains one function, is_same_class.
"""


def is_same_class(obj, a_class):
    """Returns True if the obj is exactly an instance of a_class;
    otherwise False
    """
    return type(obj) is a_class

#!/usr/bin/python3
"""The ``3-is_kind_of_class`` module

This module contains one function, is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the obj is an instances of,
    or if the ob is an instance of a class that inherited from,
    a_class; otherwise False
    """
    return isinstance(obj, a_class)

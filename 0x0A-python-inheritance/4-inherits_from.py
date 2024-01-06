#!/usr/bin/python3
"""This is ``4-inherits_from`` module
This module defines one function, inherits_from
"""


def inherits_from(obj, a_class):
    """Returns True if object is instance of a class that inherited
    (directly or indirectly) from the specified class: otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class

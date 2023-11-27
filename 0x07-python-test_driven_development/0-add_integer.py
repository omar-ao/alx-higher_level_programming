#!/usr/bin/python3
""" This is "0-add_integer" module.
This module supplies one function, add_integer(). For example,
>>> add_integer(1, 2)
3
"""
def add_integer(a, b=98):
    """Return the sum of a and b
    >>> add_integer(1, 2)
    3"""

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

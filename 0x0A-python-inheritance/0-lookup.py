#!/usr/bin/python3
"""The ``0-lookup`` module.
This module contains one function, lookup.
Usage example
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)

#!/usr/bin/python3
"""This module defines `safe_function`"""
import sys


def safe_function(fct, *args):
    """Executes a function safely"""
    try:
        result = fct(*args)
        return result
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return None

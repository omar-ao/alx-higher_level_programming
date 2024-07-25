#!/usr/bin/python3
"""This is the `safe_print_integer_err` module"""
import sys


def safe_print_integer_err(value):
    """Prints integer safely with error message"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return False

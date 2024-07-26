#!/usr/bin/python3
"""This is `102-magic_calculation.py` module"""


def magic_calculation(a, b):
    """Yet to figure out what this function does"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')

            result = result + (a ** b) / i
        except Exception as e:
            result = b + a
            break
    return result

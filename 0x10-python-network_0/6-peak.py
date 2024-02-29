#!/usr/bin/python3
"""This is `6-peak' module
It defines one function `find_peak`

Usage:
    find_peak([1, 2, 4, 6, 3])
    6
"""


def find_peak(numbers):
    """Finds the peak in a list of unsorted integers"""
    if not numbers:
        return None
    return sorted(numbers)[-1]

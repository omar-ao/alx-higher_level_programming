#!/usr/bin/python3
"""Module `103-magic_class.py`"""
import math


class MagicClass:
    """This is magic class"""

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        """Computes area"""
        return (self.radius ** 2) * math.pi

    def circumference(self):
        """Computes circumference"""
        return 2 * math.pi * self.radius

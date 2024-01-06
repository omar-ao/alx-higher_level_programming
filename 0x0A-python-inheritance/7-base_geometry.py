#!/usr/bin/python3
"""This is ``7-base_geometry`` module
It defines one class, BaseGeometry
"""


class BaseGeometry:
    """
    Defines class BaseGeometry (based on 6-base_geometry.py)
    """
    def area(self):
        """
        Compute the area of BaseGeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

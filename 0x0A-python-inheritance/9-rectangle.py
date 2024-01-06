#!/usr/bin/python3
"""This is ``9-rectangle`` module
It defines one class, BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines class Rectangle (based on 8-base_geometry.py)
    """
    def __init__(self, width, height):
        """
        Instatiates Rectangle object
        args:
        width (int): Width
        height (int) Height of the geometry
        """
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """
        Computes the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

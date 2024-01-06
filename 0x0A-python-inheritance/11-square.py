#!/usr/bin/python3
"""This is the ``11-square``
It defines a class Square that inherits from Rectangle(9-rectangle.py)
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines a class Square
    """

    def __init__(self, size):
        """
        Instantiates object from class Square
        """
        self.__size = size

        super().integer_validator("size", self.__size)

    def area(self):
        """
        Computes the area of square
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/python3
"""Class that defines square"""


class Square():
    """a class Sqaure that defines a square by:(based on 4-square.py.

    Attributes:
        size (int): size of the square
    """

    def __init__(self, size=0):
        """Initialises an instance of the class Square

        Args:
            size (int): size of the instance
        """
        self.size = size

    @property
    def size(self):
        """Gets and returns the size of the instance.

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): An integer value to set the size of the square
        Raises:
            TypeError: An error occurs when size is not integer
            ValueError: An error occurs when size is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of square

        Returns:
            int: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()

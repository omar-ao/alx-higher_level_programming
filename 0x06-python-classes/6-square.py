#!/usr/bin/python3
"""Class that defines square"""


class Square():
    """a class Sqaure that defines a square by:(based on 5-square.py.

    Attributes:
        size (int): size of the square
        position (tuple): Position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialises an instance of the class Square

        Args:
            size (int): size of the instance
            position (tuple): Position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the position of the square

        Returns:
            tuple: Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value (tuple): Position of the square
        Raises:
            TypeError: An error occurs if the position is not a tuple
            of 2 position integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        if self.position[1] > 0:
            for i in range(self.position[1]):
                print()

        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

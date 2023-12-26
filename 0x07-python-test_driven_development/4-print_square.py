#!/usr/bin/python3
"""This is ``3-print_square`` module and contains one function
Usage example:
    >>> print_square(2)
    ##
    ##
"""


def print_square(size):
    """Prints a square with the character #
    Usage example:
    >>> print_square(2)
    ##
    ##
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

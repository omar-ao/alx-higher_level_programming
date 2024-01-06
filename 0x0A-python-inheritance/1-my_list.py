#!/usr/bin/python3
"""This is ``1-my_list`` module
This module defines My_list class that inherits from list
Examples
>>> my_list = My_list()
>>> my_list.append(1)
>>> my_list.append(2)
>>> print(my_list)
[1, 2]
"""


class My_list(list):
    """A class My_list defines my_list
    """

    def print_sorted(self):
        """prints sorted list in ascending order"""
        return sorted(self)

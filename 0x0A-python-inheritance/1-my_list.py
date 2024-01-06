#!/usr/bin/python3
"""This is ``1-my_list`` module
This module defines My_list class that inherits from list
"""


class MyList(list):
    """
    A class My_list that defines my_list
    """

    def print_sorted(self):
        """prints sorted list in ascending order"""
        return sorted(self)

#!/usr/bin/python3
"""
This is the ``100-my_int`` module
It contains one class MyInt that inherits from int
"""


class MyInt(int):
    """
    Defines class MyInt that inherits from int
    """
    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True

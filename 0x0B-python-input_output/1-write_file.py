#!/usr/bin/python
"""The ``1-write_file`` module
This module contains one function, write_file
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
    the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

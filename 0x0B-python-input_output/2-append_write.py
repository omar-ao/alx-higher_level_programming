#!/usr/bin/python3
"""This is the ``2-append_write`` module
It contains one function, append_write
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(f)

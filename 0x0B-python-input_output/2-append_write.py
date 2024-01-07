#!/usr/bin/python3
"""This is the ``2-append_write`` module
It contains one function, append_write
"""


def def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(f)

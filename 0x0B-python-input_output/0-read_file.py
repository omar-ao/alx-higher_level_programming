#!/usr/bin/python3
"""The ``0-read_file`` module
This module contains one function, read_file
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text, end="")

#!/usr/bin/python3
"""This is the "5-text_indentation" module
This module supplies one function, text_indentation().
Usage example
    >>> text_indentation("This: is/ TDD.")
    This

    is

    TDD
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'
    Usage example
    >>> text_indentation("This: is/ TDD.")
    This
    <BLANKLINE>
    is
    <BLANKLINE>
    TDD
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in ".?:":
        text = (c + "\n\n").join([line.strip(" ") for line in text.split(c)])

    print(text, end="")

#!/usr/bin/python3
"""This is the ``100-append_after`` module
It defines one function, append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line
    containing a specific string
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            if search_string in line:
                f.write(line)
                f.write(new_string)
            else:
                f.write(line)

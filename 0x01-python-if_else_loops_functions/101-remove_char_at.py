#!/usr/bin/python3
def remove_char_at(str, n):
    """creates a copy of the string, removing the character at
    the position n"""
    s = []
    for i, v in enumerate(str):
        if i != n:
            s.append(v)
    return "".join(s)

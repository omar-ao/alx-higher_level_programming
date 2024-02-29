#!/usr/bin/python3

def find_peak(l):
    if not l:
        return None
    return sorted(l)[-1]

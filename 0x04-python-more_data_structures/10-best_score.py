#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = a_dictionary
    best = max(zip(a.values(), a.keys()))
    return best[1]

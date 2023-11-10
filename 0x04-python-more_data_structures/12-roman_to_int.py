#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str and len(roman_string) == 0:
        return 0
    numerals = {"I": 1,
                "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    prev = 0
    for numeral in reversed(roman_string):
        current = numerals[numeral]
        if current < prev:
            num = num - current
        else:
            num = num + current

        prev = current

    return num

#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        i = i - 32 if i in range(97, 123) else i
        print("{}".format(chr(i)), end='')
    print()

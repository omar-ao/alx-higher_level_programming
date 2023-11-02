#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    funcs = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    ops = ["+", "-", "*", "/"]

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    for op, func in zip(ops, funcs):
        if op == operator:
            print("{} {} {} = {}".format(a, op, b, func))

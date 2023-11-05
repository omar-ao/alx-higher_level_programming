#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    if not tuple_a:
        tuple_a = (0, 0)
    if not tuple_b:
        tuple_b = (0, 0)

    if len(tuple_a) == 1:
        res.append(tuple_a[0])
        res.append(0)
        tuple_a = tuple(res)

    res = []
    if len(tuple_b) == 1:
        res.append(tuple_b[0])
        res.append(0)
        tuple_b = tuple(res)

    res = []
    for i in range(2):
        res.append(tuple_a[i] + tuple_b[i])
    return (tuple(res))

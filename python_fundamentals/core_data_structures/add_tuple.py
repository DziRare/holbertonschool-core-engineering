#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    length = min(len(tuple_a), len(tuple_b))
    if length > 2:
        length = 2
    tuple_array = []

    for i in range(length):
        tuple_array.append(tuple_a[i] + tuple_b[i])

    if len(tuple_array) < 1:
        if len(tuple_a) > 1:
            tuple_array.append(tuple_a[0])
        elif len(tuple_b) > 1:
            tuple_array.append(tuple_b[0])
        else:
            tuple_array.append(0)

    if len(tuple_array) < 2:
        if len(tuple_a) > 1:
            tuple_array.append(tuple_a[1])
        elif len(tuple_b) > 1:
            tuple_array.append(tuple_b[1])
        else:
            tuple_array.append(0)

    return tuple(tuple_array)

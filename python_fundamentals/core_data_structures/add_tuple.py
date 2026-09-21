#!/usr/bin/env python3
def add_tuple(tuple_a=(), tuple_b=()):
    for _ in range(2):
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple

print(add_tuple((1, 89), (88, 11)))
#print(add_tuple((1, 89), (1, )))
# print(add_tuple((1, 89), ()))
# print(add_tuple((), ()))
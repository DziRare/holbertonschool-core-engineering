#!/usr/bin/env python3
for i in range(100):
    if i < 10:
        print("0{num}, ".format(num=i), end="")
    elif i < 99:
        print("{num}, ".format(num=i), end="")
    else:
        print("99")

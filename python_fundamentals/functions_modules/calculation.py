#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    print("{num_1} + {num_2} = {res}".format(num_1=a, num_2=b, res=add(a, b)))
    print("{num_1} - {num_2} = {res}".format(num_1=a, num_2=b, res=sub(a, b)))
    print("{num_1} * {num_2} = {res}".format(num_1=a, num_2=b, res=mul(a, b)))
    print("{num_1} / {num_2} = {res}".format(num_1=a, num_2=b, res=div(a, b)))

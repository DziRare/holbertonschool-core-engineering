#!/usr/bin/env python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    print("{result}".format(result=add(a, b)))
    print("{result}".format(result=sub(a, b)))
    print("{result}".format(result=mul(a, b)))
    print("{result}".format(result=div(a, b)))

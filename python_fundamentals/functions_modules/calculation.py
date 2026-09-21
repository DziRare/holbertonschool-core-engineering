#!/usr/bin/env python3
import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5

    print("{result}".format(result=calculator_1.add(a, b)))
    print("{result}".format(result=calculator_1.sub(a, b)))
    print("{result}".format(result=calculator_1.mul(a, b)))
    print("{result}".format(result=calculator_1.div(a, b)))

#!/usr/bin/env python3
"""This module is for reading a file"""


def read_file(filename=""):
    """This function is for reading a file"""
    with open(filename) as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")

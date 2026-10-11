#!/usr/bin/env python3
"""This module is for appending to a file"""


def append_write(filename="", text=""):
    """This function is for appending to a file"""
    with open(file=filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)


if __name__ == "__main__":
    nb_characters = append_write("file_append.txt", "This School is cool!\n")
    print(nb_characters)

#!/usr/bin/env python3
"""This module is for writing to a file"""


def write_file(filename="", text=""):
    """This function is for writing to a file"""
    with open(file=filename, mode="w", encoding="UTF-8") as f:
        return f.write(text)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is cool!\n")
    print(nb_characters)

#!/usr/bin/env python3
def uppercase(str):
    difference = ord("a") - ord("A")
    uppercase_string = ""

    for char in str:
        char_code = ord(char)
        if char_code >= ord("a") and char_code <= ord("z"):
            uppercase_char = chr(char_code - difference)
            uppercase_string += uppercase_char
        else:
            uppercase_string += char

    print("{result}".format(result=uppercase_string))

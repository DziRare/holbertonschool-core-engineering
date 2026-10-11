#!/usr/bin/env python3

def read_file(filename=""):
    with open(filename) as f:
        print(f.read())

if __name__ == "__main__":  
    read_file("my_file_0.txt")

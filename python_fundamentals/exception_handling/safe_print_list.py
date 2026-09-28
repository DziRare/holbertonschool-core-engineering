#!/usr/bin/env python3


def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            print("")
            return i
    print("")

    return x


my_list = [1, 2, 3, 4]

nb_print = safe_print_list(my_list, 6)
print(f"elements: {nb_print}")

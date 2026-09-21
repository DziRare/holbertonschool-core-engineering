#!/usr/bin/env python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    max_score = 0
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_key = key

    return max_key

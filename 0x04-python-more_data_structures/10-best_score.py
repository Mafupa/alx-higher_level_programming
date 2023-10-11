#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    big = 0
    for key in a_dictionary.keys():
        if big == 0:
            big = key
        if a_dictionary[key] > a_dictionary[big]:
            big = key
    return big

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    new = [key for key, val in a_dictionary.items() if val == value]
    for i in new:
        del a_dictionary[i]
    return a_dictionary

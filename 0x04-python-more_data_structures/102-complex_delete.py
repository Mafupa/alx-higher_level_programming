#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = {}
    for key in a_dictionary.keys():
        if a_dictionary[key] != value:
            new[key] = a_dictionary[key]
    #a_dictionary = new
    return new

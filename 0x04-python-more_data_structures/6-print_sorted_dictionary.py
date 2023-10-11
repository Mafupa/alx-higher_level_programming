#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for key in sorted(list(a_dictionary.keys())):
        print("{} : {}".format(key, a_dictionary[key]))

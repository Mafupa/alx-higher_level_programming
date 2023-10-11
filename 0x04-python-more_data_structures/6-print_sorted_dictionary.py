#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in list(a_dictionary.keys()).sort():
        print("{} : {}".format(key, a_dictionary[key]))

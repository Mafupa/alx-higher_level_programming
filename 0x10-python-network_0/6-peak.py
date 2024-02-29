#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    li = list_of_integers
    if len(li) == 1:
        return li[0]
    for i in range(len(li)-1):
        if i == 0:
            if li[i+1] < li[i]:
                return li[i]
            continue
        if li[i-1] < li[i] > li[i+1]:
            return li[i]
    return li[-1]

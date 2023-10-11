#!/usr/bin/python3
def uniq_add(my_list=[]):
    used = []
    tot = 0
    for i in my_list:
        if i not in used:
            tot += i
            used.append(i)
    return tot

#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str):
        return 0
    tot = 0
    crs = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for i in range(len(roman_string)):
        tot += crs[roman_string[i]]
        for j in range(i,len(roman_string)):
            if crs[roman_string[i]] < crs[roman_string[j]]:
                tot -= crs[roman_string[i]] * 2
                break
    return tot
        

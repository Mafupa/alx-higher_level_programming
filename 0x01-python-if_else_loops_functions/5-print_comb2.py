#!/usr/bin/python3
for i in range(99):
    print("{i:02d}".format(i), end=', ')
print("{i+1:02d}".format(i))

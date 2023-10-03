#!/usr/bin/python3
for i in range(90, 64, -1):
    print("{}".format(chr(i+(32*((i+1) % 2)))), end='')

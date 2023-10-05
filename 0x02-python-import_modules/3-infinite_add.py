#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    tot = 0
    for i in range(1, argc):
        tot += int(argv[i])
    print(tot)

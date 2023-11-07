#!/usr/bin/python3
"""readfile"""


def read_file(filename=""):
    """readfile"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')

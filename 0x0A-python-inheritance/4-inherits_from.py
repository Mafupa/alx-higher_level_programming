#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """inherits from"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

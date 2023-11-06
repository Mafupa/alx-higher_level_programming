#!/usr/bin/python3
"""MyInt"""


class MyInt(int):
    """MyInt"""
    def __eq__(self, value):
        """eq"""
        return self.real != value

    def __ne__(self, value):
        """ne"""
        return self.real == value

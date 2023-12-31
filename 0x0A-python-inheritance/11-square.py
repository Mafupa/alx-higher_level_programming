#!/usr/bin/python3
"""Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """"area"""
        return self.size ** 2

    def __str__(self):
        """str"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

#!/usr/bin/python3
"""Square class"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """init"""
        self.__size = size

    @property
    def size(self):
        """no time"""
        return self.__size

    @size.setter
    def size(self, size):
        """no time"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """no time"""
        return self.__size ** 2

    def my_print(self):
        """no time"""
        for i in range(self.__size):
            print("#"*self.__size)
        if self.__size == 0:
            print("")

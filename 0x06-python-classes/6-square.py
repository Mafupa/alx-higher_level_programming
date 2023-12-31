#!/usr/bin/python3
"""Square class"""


class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """init"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """no time"""
        return self.__position

    @position.setter
    def position(self, value):
        """no time"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """no time"""
        return self.__size ** 2

    def my_print(self):
        """no time"""
        if self.__size == 0:
            print("")
            return
        [print("") for x in range(self.__position[1])]
        for i in range(self.__size):
            print(" "*self.__position[0], end='')
            print("#"*self.__size)

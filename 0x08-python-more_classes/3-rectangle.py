#!/usr/bin/python3
"""no time"""


class Rectangle:
    """no time"""
    def __init__(self, width=0, height=0):
        """no time"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """no time"""
        return self.__width

    @width.setter
    def width(self, value):
        """no time"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """no time"""
        return self.__height

    @height.setter
    def height(self, value):
        """no time"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            string +=  ("#" * self.__width) + ("\n" if i != self.__height - 1 else "")
        return string

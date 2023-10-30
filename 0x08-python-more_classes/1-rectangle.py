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



#!/usr/bin/python3
""""Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
   """Rectangle"""
   def __init__(self, width, height):
       """init"""
       self.integer_validator("width", width)
       self.__width = width
       self.integer_validator("height", height)
       self.__height = height

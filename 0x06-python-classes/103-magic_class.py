#!/usr/bin/python3
"""provides a magicclass matching the given bytecode"""


import math

class MagicClass:
    """
    A class representing a magical circle with radius and related calculations.
    """

    def __init__(self, radius):
        """
        Initializes a new MagicClass instance.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magical circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the magical circle.
        """
        return 2 * math.pi * self.__radius


"""
Vi skapar vår egen modul som kan importeras till andra filer.
Återanvändningsbar funktion.
importeras med import math_functions

eller

from math_functions import calculate_cylinder_volume
"""

import math


def calculate_cylinder_volume(radius, height):
    return math.pi * radius * 2 * height

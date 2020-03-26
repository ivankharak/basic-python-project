#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

"""
Define a class 'Circle' which can be constructed by either radius or diameter.
The 'Circle' class has a method which can compute the area and perimeter.
"""

import math


class Circle:
    def __init__(self, radius=0, diameter=0):
        self.radius = radius
        self.diameter = diameter

    def _area(self):
        if self.diameter:
            self.radius = self.diameter / 2
        return math.pi * (self.radius * self.radius)

    def _perimeter(self):
        if self.diameter:
            self.radius = self.diameter / 2
        return 2 * math.pi * self.radius

    def compute(self):
        return [self._area(), self._perimeter()]


if __name__ == "__main__":
    c = Circle(diameter=10)
    print(f"Area of Cricle: {c.compute()[0]} \nPerimeter of Circle: {c.compute()[1]}")

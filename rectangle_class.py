#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

"""
Define a class 'Rectangle' which can be constructed by length and
width. The 'Rectangle' class has a method which can compute
the area.
"""


class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


if __name__ == "__main__":
    rectangle = Rectangle(5, 15)
    print("Area of Rectangle:", rectangle.area())

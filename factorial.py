#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

"""
Write a program which can compute the factorial of a given number
"""


from math import factorial
from operator import mul
from functools import reduce
from scipy.special import factorial as scipy_fact


def math_factorial(num):
    return factorial(num)


def fcktorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact *= i  # same as fact = fact * i
    return fact


def mul_factorial(num):
    return reduce(mul, range(1, num + 1))


def scipy_factorial(num):
    return scipy_fact(num)


def lambda_factorial(num):
    return reduce((lambda x, y: x * y), range(1, num + 1))


if __name__ == "__main__":
    ask = input("NUMBER: ")
    print(f"Factorial of {ask} is {math_factorial(int(ask))}")

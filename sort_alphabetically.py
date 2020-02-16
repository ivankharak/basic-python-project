#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

"""
Write a program that accepts a comma seperated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically. 
"""

import re


def to_sort_simple(sequence):
    return sorted(sequence.split(","))


def to_sort(sequence):
    s = re.sub(r"\s|\t", "", sequence).split(",")
    # strips tabs and newlines and splits by comma
    s.sort(key=lambda x: re.sub(r"\d", "", x).lower())
    # ignores any digits in the each string in the list
    return ", ".join(s)


if __name__ == "__main__":
    ask = input("ENTER COMMA-SEPERATED SEQUENCE: ")
    print(f"[RESULT] Your sequence, alphabetically sorted: {to_sort(ask)}")

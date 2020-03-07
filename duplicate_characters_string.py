#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from collections import Counter

s = "Andaman and Nicobar"
chars = []

for i in s:
    if i not in chars:
        chars.append(i)

dupes = [i for idx, i in enumerate(Counter(chars)) if idx > 1]
print(dupes)

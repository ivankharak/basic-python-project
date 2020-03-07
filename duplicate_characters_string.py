#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from collections import Counter

s = "Andaman and Nicobar"
chars = Counter(s.lower())

dupes = [k for k, v in chars.items() if v > 1]

print(dupes)

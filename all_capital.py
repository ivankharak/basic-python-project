#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

"""
Write a program that accept a sequence of lines* and prints the lines
as input and prints the lines after making all the characters
in the sequence capitalized.

*blank line or CTRL+D to terminate
"""

import sys


def all_caps():
    lines = list()
    while True:
        sequence = input()
        if sequence:
            lines.append(str(sequence.upper()))
        else:
            break
    return "\n".join(lines)


def all_caps_eof():
    print("[CTRL+D] to Save & Generate Output")
    lines = list()
    while True:
        try:
            sequence = input()
        except EOFError:
            break
        lines.append(str(sequence.upper()))
    return "\n".join(lines)


def all_caps_readlines():
    print("[CTRL+D] to Save & Generate Output")
    lines = sys.stdin.readlines()
    return f"\n\nALL CAPS:\n {' '.join(lines).upper()}"
    # use single quotes w/ .join() when using it in fstring


if __name__ == "__main__":
    print(all_caps_readlines())

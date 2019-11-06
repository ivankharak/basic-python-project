#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry


def get_data():
    _string = input("Enter string to reverse: ")
    return _string


def reversed_string(_string):
    strng = str(_string)
    return strng[::-1]


def alternative(_string):
    strng = "".join(reversed(_string))
    return strng


def list_reverse(_string):
    l = list(_string)
    l.reverse()
    return "".join(l)


if __name__ == "__main__":
    string_to_reverse = get_data()
    print(reversed_string(string_to_reverse))
    print(alternative(string_to_reverse))
    print(list_reverse(string_to_reverse))

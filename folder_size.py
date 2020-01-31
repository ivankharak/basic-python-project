#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from subprocess import run
from prettytable import PrettyTable

# PS: This only works on macOS & Linux. It will not work on Windows
# unless you install GNU coreutils:
# http://gnuwin32.sourceforge.net/packages/coreutils.htm


def folder_size(path):
    size = run(["du", "-sk", path], capture_output=True, encoding="utf-8")
    return size


def megabytes(size):
    mb = int(size) / 1024
    return round(mb, 2)


def gigabytes(size):
    gb = (int(size) / 1024) / 1024
    return round(gb, 2)


def table_print(data):
    t = PrettyTable()
    mb = megabytes(data[0])
    gb = gigabytes(data[0])
    t.field_names = ["Folder/Directory", "KB", "MB", "GB"]
    t.add_row([data[1], data[0], mb, gb])
    print(t)


if __name__ == "__main__":
    try:
        s = folder_size(input("PATH TO FOLDER/DIR: "))
        s = str(s.stdout).split("\t")
        table_print(s)
    except ValueError:
        print("Please enter a valid PATH without quotes or any other characters")

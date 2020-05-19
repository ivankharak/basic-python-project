#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        status = True
    elif year % 100 == 0 and year % 400 == 0:
        status = True
    else:
        status = False
    return status


if __name__ == "__main__":
    print(list(map(is_leap_year, [100, 400, 1800, 1900, 2000, 2020])))

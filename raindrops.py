#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def raindrops(num):
    res = ""
    if num % 3 == 0:
        res += "Pling"
    if num % 5 == 0:
        res += "Plang"
    if num % 7 == 0:
        res += "Plong"
    return num if not res else res


def raindrops_list_comp(num):
    drops = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    res = [word for factor, word in drops if not num % factor]
    return num if not res else "".join(res)


if __name__ == "__main__":
    print(raindrops(105))
    print(raindrops_list_comp(105))

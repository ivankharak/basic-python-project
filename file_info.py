#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry


from os import stat, path
from datetime import datetime
from prettytable import PrettyTable


def file_info(_path):
    s = stat(_path)
    d = {}
    d["path"] = _path
    d["size"] = s.st_size  # bytes
    d["byte_blocks"] = s.st_blocks  # no. of 512-byte blocks allocated for file
    tstamps = tuple(
        map(
            datetime.fromtimestamp,
            (int(s.st_atime), int(s.st_mtime), int(s.st_ctime), int(s.st_birthtime)),
        )
    )
    d["last_accessed"], d["last_modified"], d["last_created"], d["birthtime"] = tstamps
    return d


def file_ext(_path):
    _, ext = path.splitext(_path)
    return ext


def table(data):
    t = PrettyTable()
    t.field_names = [
        "PATH/FILE",
        "SIZE",
        "EXT",
        "LAST ACCESSED",
        "LAST MODIFIED",
        "LAST CREATED",
    ]
    t.add_row(
        [
            data["path"],
            data["size"],
            file_ext(data["path"]),
            data["last_accessed"],
            data["last_modified"],
            data["last_created"],
        ]
    )
    print(t)


if __name__ == "__main__":
    p = file_info(input("PATH TO FILE: "))
    table(p)

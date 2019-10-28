# !/usr/bin/env

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from prettytable import PrettyTable
from click import prompt


def take_input():
    number = prompt("Number? ", type=int)
    table_range = prompt("Table Range?", type=int)
    return number, table_range


# For validation, if you don't want to use Click: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response


def multitable(number, table_range):
    column_one = []
    column_two = []

    for i in range(1, table_range + 1):
        column_one.append(" x ".join([str(number), str(i)]))
        column_two.append(i * number)

    return column_one, column_two


def output(data):
    column_one, column_two = data  # tuple unpacking:
    table = PrettyTable()
    table.add_column("x", column_one)
    table.add_column("Result", column_two)
    print(table)


if __name__ == "__main__":
    number, table_range = take_input()
    data = multitable(number, table_range)
    output(data)

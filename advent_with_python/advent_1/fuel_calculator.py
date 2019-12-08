#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate_fuel(mass):
    return (mass // 3) - 2


def read_modules(path: str) -> list:
    lines = list()
    with open(path) as fs:
        for line in fs.readlines():
            if line:
                lines.append(int(line))

    return lines


def do_all_fuels(masses: list):
    return sum([masses.append(calculate_fuel(x)) or calculate_fuel(x) for x in masses if (calculate_fuel(x)) > 0])


def do_only_fuels(masses: list) -> int:
    return sum([calculate_fuel(x) for x in masses if (calculate_fuel(x)) > 0])


if __name__ == "__main__":
    massses = read_modules("../input_1.txt")
    print("Ergebnis für Part1: "+str(do_only_fuels(massses.copy()))+" Liter")
    do_all_fuels(massses.copy())
    print("Ergebnis für Part2: "+str(do_all_fuels(massses.copy()))+" Liter")


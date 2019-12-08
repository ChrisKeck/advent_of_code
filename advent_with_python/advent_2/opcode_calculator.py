#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_modules(path: str) -> list:
    lines = list()
    with open(path) as fs:
        for line in fs.read().split(","):
            if line:
                lines.append(int(line))

    return lines


def group(lsttogrp, n):
    return zip(*[lsttogrp[i::n] for i in range(n)])


if __name__ == "__main__":
    lst = read_modules("../input_2.txt")
    grplst = group(lst.copy(), 4)
    for opcode, pos_one, pos_two, pos_res in grplst:
        res = -1
        if opcode == 1:
            lst[pos_res] = lst[pos_one] + lst[pos_two]
        elif opcode == 2:
            lst[pos_res] = lst[pos_one] * lst[pos_two]
        else:
            break
    print(lst)

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


def puzzle_two():
    goal = 19690720

    with open('..//input_2.txt') as file:
        input = list(map(lambda a: int(a), file.read().split(',')))

    found = False
    for noun in range(100):
        for verb in range(100):
            memory = input[:]
            memory[1] = noun
            memory[2] = verb

            opcode, index = int(input[0]), 0
            while opcode != 99:
                if opcode == 1:
                    sum = memory[memory[index + 1]] + memory[memory[index + 2]]
                    memory[memory[index + 3]] = sum
                elif opcode == 2:
                    product = memory[memory[index + 1]] * memory[memory[index + 2]]
                    memory[memory[index + 3]] = product
                elif opcode != 99:
                    print('Something went wrong')

                index += 4
                opcode = memory[index]

            output = memory[0]

            if output == goal:
                final_noun = noun
                final_verb = verb
                found = True
                break
        if found == True:
            break
    print(f'Puzzle 2 - {100 * final_noun + final_verb}')


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
    puzzle_two()

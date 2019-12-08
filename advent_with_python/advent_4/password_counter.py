#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_ascending(password):
    return "".join(sorted(password)) == password


def is_repeated(password):
    for digit1, digit2 in zip(password, password[1:]):
        if digit1 == digit2:
            return True


def are_two_consecutive_digits(password):
    repeat_count = 0
    for n1, n2 in zip(password, password[1:]):
        if n1 == n2:
            repeat_count += 1
        else:
            if repeat_count == 1:
                return True
            repeat_count = 0
    return repeat_count == 1


def get_count_for_part_one(begin, end):
    count = 0
    for number in range(begin, end):
        number = str(number)
        if is_ascending(number) and is_repeated(number):
            count += 1
    return count


def get_count_for_part_two(begin, end):
    count = 0
    for number in range(begin, end):
        number = str(number)
        if is_ascending(number) and are_two_consecutive_digits(number):
            count += 1
    return count


if __name__ == "__main__":
    p1_count = get_count_for_part_one(234208, 765869)
    print(f"Part 1: {p1_count}")

    p2_count = get_count_for_part_two(234208, 765869)
    print(f"Part 2: {p2_count}")

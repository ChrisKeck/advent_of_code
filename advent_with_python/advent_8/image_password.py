#!/usr/bin/env python
# -*- coding: utf-8 -*-


def split(lst, image_size):
    return [lst[i:i + image_size] for i in range(0, len(lst), image_size)]


def count(image_layer, mode):
    return sum(map(lambda x: 1 if x == mode else 0, image_layer))


def collapse(image_layers):
    return [next(filter(lambda v: v != 2, lay)) for lay in zip(*image_layers)]


def draw(image):
    for r in image:
        print(*['#' if x == 1 else ' ' for x in r])


def extract_layers(x, y):
    size = lenx * leny
    data = [int(x) for x in open('../input_8.txt').read().strip('\n')]
    return split(data, size)


def get_count_for_part_one(image_layers):
    best = min(image_layers, key=lambda layer: count(layer, 0))
    return count(best, 1) * count(best, 2)


def draw_for_part_two(image_layers, x):
    img = split(collapse(image_layers), x)
    draw(img)


if __name__ == "__main__":
    lenx = 25
    leny = 6
    layers = extract_layers(lenx, leny)

    result = get_count_for_part_one(layers)
    print(f"Part1: {result}")

    draw_for_part_two(layers, lenx)

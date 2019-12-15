import collections
import re


def get_inputs(f):
    lines = [line.rstrip('\n') for line in f]
    lines = [[i for i in re.findall(r'-?\d+|[A-Z]+', line)] for line in lines]
    inputs = {}
    for line in lines:
        co, cq = line[-2:]
        co = int(co)
        ins = []
        for first, second in zip(line[:-2][::2], line[:-2][1::2]):
            ins.append((int(first), second))
        assert cq not in inputs
        inputs[cq] = (co, ins)
    return inputs


def try_fuel_part_one(fuel, inputs):
    need = {'FUEL': fuel}
    have = collections.defaultdict(int)
    while True:
        try:
            nk = next(n for n in need if n != 'ORE')
        except StopIteration:
            break
        quant, ins = inputs[nk]
        d, m = divmod(need[nk], quant)
        if m == 0:
            del need[nk]
        else:
            del need[nk]
            have[nk] = quant - m
            d += 1
        for first, second in ins:
            need[second] = need.get(second, 0) + d * first - have[second]
            del have[second]
    return need['ORE']


def try_fuel_part_two(inputs):
    first, second = 1, 2
    while try_fuel_part_one(second, inputs) < 10 ** 12:
        first, second = second, second * 2
    while second - first >= 2:
        half = first + (second - first) // 2
        if try_fuel_part_one(half, inputs) > 10 ** 12:
            second = half
        else:
            first = half
    return first


if __name__ == "__main__":
    with open("../input_14.txt") as f:
        outs = get_inputs(f)
        print(try_fuel_part_one(1, outs))

        print(try_fuel_part_two(outs))

import itertools
import functools
import operator


def calculate(combo_length):
    for combo in itertools.combinations(numbers, combo_length):
        if functools.reduce(operator.add, combo) == 2020:
            return functools.reduce(operator.mul, combo)


with open("01.txt") as _input:
    numbers = [int(x) for x in _input.readlines()]

print([calculate(x) for x in [2, 3]])

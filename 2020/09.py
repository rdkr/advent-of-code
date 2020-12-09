import itertools

with open("09.txt") as _input:
    numbers = [int(line) for line in _input]


def part_one(preamble):
    for i in range(preamble, len(numbers)):
        pairs = itertools.permutations(numbers[i - preamble : i], 2)
        if not numbers[i] in [sum(pair) for pair in pairs]:
            return numbers[i]


def part_two(target):
    index, size = 0, 3
    while True:
        chunk = numbers[index : index + size]
        if sum(chunk) == target:
            return min(chunk) + max(chunk)
        if index == len(numbers) - size:
            size = size + 1
            index = 0
        else:
            index = index + 1


invalid = part_one(25)
print(invalid, part_two(invalid))

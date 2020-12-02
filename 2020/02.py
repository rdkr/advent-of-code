import collections

Entry = collections.namedtuple("Entry", ["param_1", "param_2", "char", "value"])


def line_to_entry(line):
    key, value = line.split(": ")
    params, char = key.split(" ")
    param_1, param_2 = params.split("-")
    return Entry(int(param_1), int(param_2), char, value.rstrip())


def validate_1(entry):
    return entry.param_1 <= entry.value.count(entry.char) <= entry.param_2


def validate_2(entry):
    first_match = entry.value[entry.param_1 - 1] == entry.char
    second_match = entry.value[entry.param_2 - 1] == entry.char
    return first_match ^ second_match


result_1, result_2 = 0, 0

with open("02.txt") as _input:
    for line in _input:
        entry = line_to_entry(line)
        result_1 += validate_1(entry)
        result_2 += validate_2(entry)

print(result_1, result_2)

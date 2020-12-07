import itertools


def cards():
    card = []
    with open("06.txt") as _input:
        for line in _input:
            if row := line.rstrip():
                card.append(row)
            else:
                yield card
                card = []
        yield card


one, two = 0, 0
for card in cards():
    one = one + len(set(itertools.chain(*card)))
    two = two + len(set.intersection(*[set(entry) for entry in card]))
print(one, two)

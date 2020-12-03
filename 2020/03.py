def lines(y):
    i_line = 0
    with open("03.txt") as _input:
        for line in _input:
            if not i_line % y:
                yield line.rstrip()
            i_line = i_line + 1


def trees(x, y):
    i_x, i_y, trees = 0, 0, 0
    for line in lines(y):
        if line[i_x % len(line)] == "#":
            trees = trees + 1
        i_x = i_x + x
    return trees


print(trees(3, 1))
print(trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2))

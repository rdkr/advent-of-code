from itertools import count
from dataclasses import dataclass, field


@dataclass
class Tree:
    height: int
    id: int = field(default_factory=count().__next__, init=False)


def check_grid(grid, indexes):
    trees = set()
    for index in indexes:
        last = -1
        for i in index:
            if grid[i].height > last:
                trees.add(grid[i].id)
                last = grid[i].height
    return trees


def main():

    grid = []

    with open("inputs/08.txt", "r") as _input:
        trees = _input.read().splitlines()

    x = len(trees)
    y = len(trees[0])

    l2r = [[j + x * i for j in range(y)] for i in range(x)]
    r2l = [line[::-1] for line in l2r]
    t2b = [[i + x * j for j in range(y)] for i in range(x)]
    b2t = [line[::-1] for line in t2b]

    for line in trees:
        grid.extend([Tree(int(height)) for height in line])

    print(
        len(
            check_grid(grid, l2r)
            | check_grid(grid, r2l)
            | check_grid(grid, t2b)
            | check_grid(grid, b2t)
        )
    )


if __name__ == "__main__":
    main()

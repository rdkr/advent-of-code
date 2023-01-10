import itertools
import math


class Knot:
    def __init__(self):
        self.x = self.y = 0
        self.history = set()

def floor_ceil(x):
    if math.isclose(0, x, abs_tol=1e-10):
        return 0
    else:
        return math.ceil(x) if x > 0 else math.floor(x)


def main():

    with open("inputs/09.txt", "r") as _input:
        moves = [move.split(" ") for move in _input.read().splitlines()]

    knots = [Knot() for _ in range(10)]

    for direction, steps in moves:
        for _ in range(int(steps)):

            if direction == "U":
                knots[0].y += 1
            elif direction == "D":
                knots[0].y -= 1
            elif direction == "L":
                knots[0].x -= 1
            elif direction == "R":
                knots[0].x += 1

            for head, tail in itertools.pairwise(knots):
                diff_x = head.x - tail.x
                diff_y = head.y - tail.y
                if math.sqrt(diff_x * diff_x + diff_y * diff_y) >= 2:
                    atan2 = math.atan2(diff_y, diff_x)
                    tail.x += floor_ceil(math.cos(atan2))
                    tail.y += floor_ceil(math.sin(atan2))
                tail.history.add((tail.x, tail.y))

    print(len(knots[1].history), len(knots[9].history))


if __name__ == "__main__":
    main()

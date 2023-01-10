import numpy as np


def main():

    trees = np.genfromtxt("inputs/08.txt", dtype=int, delimiter=1)
    x, y = trees.shape
    visible = x * 2 + y * 2 - 4
    max_scenic_score = 0

    for i in range(1, x - 1):
        for j in range(1, y - 1):

            tree = trees[i, j]

            left = trees[i, :j][::-1]
            right = trees[i, j + 1 :]
            up = trees[:i, j][::-1]
            down = trees[i + 1 :, j]

            if (
                np.all(left < tree)
                or np.all(right < tree)
                or np.all(up < tree)
                or np.all(down < tree)
            ):
                visible += 1

            direction_scores = []
            for direction in left, right, up, down:
                direction_score = 0
                for nearby in direction:
                    direction_score += 1
                    if tree <= nearby:
                        break
                direction_scores.append(direction_score)

            scenic_score = np.prod(direction_scores)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(visible, max_scenic_score)


if __name__ == "__main__":
    main()

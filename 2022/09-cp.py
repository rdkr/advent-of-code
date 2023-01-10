class Knot:
    def __init__(self):
        self.x = self.y = 0


def main():

    with open("inputs/09.txt", "r") as _input:
        moves = [move.split(" ") for move in _input.read().splitlines()]

    head_x = head_y = tail_x = tail_y = 0
    history = {(tail_x, tail_y)}

    for direction, steps in moves:
        print(direction, steps)
        for _ in range(int(steps)):
            if direction == "U":
                head_y += 1
                tail_x = head_x if head_y - tail_y > 1 else tail_x
                tail_y = head_y - 1 if head_y - tail_y > 1 else tail_y
            elif direction == "D":
                head_y -= 1
                tail_x = head_x if head_y - tail_y < -1 else tail_x
                tail_y = head_y + 1 if head_y - tail_y < -1 else tail_y
            elif direction == "L":
                head_x -= 1
                print("DEBUG", head_x - tail_x, head_x - tail_x < -1)
                tail_y = head_y if head_x - tail_x < -1 else tail_y
                tail_x = head_x + 1 if head_x - tail_x < -1 else tail_x
                print("EEE", head_y, tail_y)
            elif direction == "R":
                head_x += 1
                tail_y = head_y if head_x - tail_x > 1 else tail_y
                tail_x = head_x - 1 if head_x - tail_x > 1 else tail_x

            history.add((tail_x, tail_y))

            print(head_x, head_y, tail_x, tail_y)
            print()

    print(history)
    print(len(history))


if __name__ == "__main__":
    main()

# if diff_x == 2:
#     tail.y += 1
# elif diff_x > 1 and diff_y < -1:
#     tail.x += 1
#     tail.y += 1
# elif diff_y == 2:
#     tail.y += 1
# elif diff_x < -1 and diff_y < -1:
#     tail.x += 1
#     tail.y -= 1
# elif diff_x == -2:
#     tail.y += 1
#
# elif diff_x < -1 and diff_y > 1:
#     ...
# elif diff_y == -2:
#     ...
# elif diff_x < -1 and diff_y > 1:

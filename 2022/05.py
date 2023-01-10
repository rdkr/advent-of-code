from collections import defaultdict


def main():

    stacks_p1 = defaultdict(list)
    stacks_p2 = defaultdict(list)

    with open("inputs/05.txt", "r") as _input:
        lines = _input.read().splitlines()

    for line in lines:

        if line.startswith(" 1") or line == "":
            continue

        if line.startswith("move"):
            instruction = line.split(" ")

            amount = int(instruction[1])
            source = int(instruction[3])
            destination = int(instruction[5])

            p2_moving_stack = []
            for i in range(amount):
                stacks_p1[destination].insert(0, stacks_p1[source].pop(0))
                p2_moving_stack.append(stacks_p2[source].pop(0))

            stacks_p2[destination] = p2_moving_stack + stacks_p2[destination]
            continue

        for i, char in enumerate(line):
            if not (i - 1) % 4 and not char == " ":
                stacks_p1[(i - 1) // 4 + 1].append(char)
                stacks_p2[(i - 1) // 4 + 1].append(char)

    print("".join(x[0] for x in dict(sorted(stacks_p1.items())).values()))
    print("".join(x[0] for x in dict(sorted(stacks_p2.items())).values()))


if __name__ == "__main__":
    main()

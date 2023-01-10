def main():

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total_p1 = total_p2 = 0

    with open("inputs/03.txt", "r") as _input:
        backpacks = _input.read().splitlines()

    for backpack in backpacks:
        compartments = [
            set(backpack[: len(backpack) // 2]),
            set(backpack[len(backpack) // 2 :]),
        ]
        for item in set.intersection(*compartments):
            total_p1 += alphabet.index(item) + 1

    for i in range(len(backpacks) // 3):
        trio = [set(backpack) for backpack in backpacks[i * 3 : i * 3 + 3]]
        for item in set.intersection(*trio):
            total_p2 += alphabet.index(item) + 1

    print(total_p1, total_p2)


if __name__ == "__main__":
    main()

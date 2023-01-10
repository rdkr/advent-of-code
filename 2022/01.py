def main():

    calories = [0]

    with open("inputs/01.txt", "r") as _input:
        for line in _input:
            if line.strip() != "":
                calories[-1] += int(line)
            else:
                calories.append(0)

    calories.sort()
    print(calories[-1], sum(calories[-3:]))


if __name__ == "__main__":
    main()

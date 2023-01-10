def main():

    total_p1 = total_p2 = 0

    with open("inputs/04.txt", "r") as _input:
        lines = _input.read().splitlines()

    for line in lines:
        first_start, first_end, second_start, second_end = [
            int(x) for x in line.replace("-", ",").split(",")
        ]

        if (first_start <= second_start and first_end >= second_end) or (
            second_start <= first_start and second_end >= first_end
        ):
            total_p1 += 1

        if (
            (second_start <= first_start <= second_end)
            or (first_start <= second_start <= first_end)
            or (second_start <= first_end <= second_end)
            or (first_start <= second_end <= first_end)
        ):
            total_p2 += 1

    print(total_p1, total_p2)


if __name__ == "__main__":
    main()

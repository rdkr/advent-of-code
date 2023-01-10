def main():

    abc = "ABC"
    xyz = "XYZ"

    score_p1 = 0
    score_p2 = 0

    with open("inputs/02.txt", "r") as _input:
        for line in _input:
            opponent, me = line.strip().split(" ")

            if abc.index(opponent) == xyz.index(me):  # draw
                score_p1 += 3
            elif abc.index(opponent) == (xyz.index(me) - 1) % 3:  # win
                score_p1 += 6
            score_p1 += xyz.index(me) + 1

            if me == "Y":  # draw
                score_p2 += 3
                score_p2 += xyz.index(xyz[abc.index(opponent)]) + 1
            elif me == "Z":  # win
                score_p2 += 6
                score_p2 += xyz.index(xyz[(abc.index(opponent) + 1) % 3]) + 1
            else:  # lose
                score_p2 += xyz.index(xyz[(abc.index(opponent) - 1) % 3]) + 1

    print(score_p1, score_p2)


if __name__ == "__main__":
    main()

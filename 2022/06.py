def check_stream(stream, distinct_characters):
    for i in range(distinct_characters, len(stream)):
        if len(set(stream[i - distinct_characters : i])) == distinct_characters:
            return i


def main():
    with open("inputs/06.txt", "r") as _input:
        stream = _input.read()
    print(check_stream(stream, 4), check_stream(stream, 14))


if __name__ == "__main__":
    main()

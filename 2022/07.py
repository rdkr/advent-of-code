class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parents = [parent] + parent.parents if parent else []
        self.size = 0
        self.directories = {}
        self.files = []

    def find_directories(self, check):
        directories = []
        for directory in self.directories.values():
            if check(directory):
                directories.append(directory)
            directories.extend(directory.find_directories(check))
        return directories


def main():

    with open("inputs/07.txt", "r") as _input:
        stream = _input.read().splitlines()

    root = Directory("/")
    current = root

    for line in stream[1:]:
        match line.split():
            case ["$", "cd", ".."]:
                current = current.parents[0]
            case ["$", "cd", directory]:
                current = current.directories[directory]
            case ["$", "ls"]:
                continue
            case ["dir", directory]:
                current.directories[directory] = Directory(directory, current)
            case _:
                size, filename = line.split(" ")
                current.files.append((filename, int(size)))
                for directory in [current] + current.parents:
                    directory.size += int(size)

    small_directories = root.find_directories(
        lambda directory: directory.size <= 100000
    )
    print(sum(directory.size for directory in small_directories))

    delete_at_least = 30000000 - (70000000 - root.size)
    delete_candidates = root.find_directories(
        lambda directory: directory.size >= delete_at_least
    )
    print(sorted(delete_candidates, key=lambda directory: directory.size)[0].size)


if __name__ == "__main__":
    main()

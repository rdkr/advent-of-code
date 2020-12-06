def solve(string, add_char, exp):
    pos = 0
    for char in string:
        if char == add_char:
            pos = pos + 2 ** exp
        exp = exp - 1
    return pos


with open("05.txt") as _input:
    ids = [solve(line[:7], "B", 6) * 8 + solve(line[7:], "R", 2) for line in _input]
print(max(ids), [seat for seat in range(min(ids), max(ids)) if seat not in ids])

def passports():
    passport = {}
    with open("04.txt") as _input:
        for line in _input:
            if row := line.rstrip():
                for data in row.split(" "):
                    k, v = data.split(":")
                    passport[k] = v
            else:
                yield passport
                passport = {}
        yield passport


def validate(passport):
    fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    if step_one := fields.issubset(set(passport.keys())):
        try:
            step_two = all(
                [
                    1920 <= int(passport["byr"]) <= 2002,
                    2010 <= int(passport["iyr"]) <= 2020,
                    2020 <= int(passport["eyr"]) <= 2030,
                    (
                        150 <= int(passport["hgt"][:-2]) <= 193
                        and passport["hgt"][-2:] == "cm"
                        or 59 <= int(passport["hgt"][:-2]) <= 76
                        and passport["hgt"][-2:] == "in"
                    ),
                    passport["hcl"][0] == "#" and int(passport["hcl"][1:], 16),
                    passport["ecl"]
                    in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                    int(passport["pid"]) and len(passport["pid"]) == 9,
                ]
            )
        except:
            return step_one, False
        return step_one, step_two
    return step_one, False


step_one, step_two = 0, 0
for result in (validate(x) for x in passports()):
    step_one = step_one + result[0]
    step_two = step_two + result[1]
print(step_one, step_two)

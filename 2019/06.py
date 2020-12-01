import collections

with open("06.txt", "r") as f:
    orbits_list = f.read().splitlines()

orbits = {}
for orbit in orbits_list:
    name, sat_name = orbit.split(')')
    orbits[sat_name] = name

paths_to_root = collections.defaultdict(lambda: set(('COM',)))
for k, v in orbits.items():
    current = k
    while current != 'COM':
        current = orbits[current]
        paths_to_root[k].add(current)

print(sum([len(x) for x in paths_to_root.values()]))
print(len(paths_to_root['YOU'] ^ paths_to_root['SAN']))

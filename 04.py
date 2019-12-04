pw_min, pw_max = (int(x) for x in "240298-784956".split("-"))

from collections import defaultdict


def valid(i):
  doubles = defaultdict(int)
  last = 0
  for c in str(i):
    if int(c) == last:
      doubles[c] += 1
    if int(c) < last:
      return False, False
    last = int(c)
  return bool(doubles), bool(1 in doubles.values())


pw1_valid = pw2_valid = 0
for x in range(pw_min, pw_max):
  pw1, pw2 = valid(x)
  pw1_valid = pw1_valid + pw1
  pw2_valid = pw2_valid + pw2

print(pw1_valid, pw2_valid)

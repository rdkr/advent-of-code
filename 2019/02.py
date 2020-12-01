raw_data = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0"

import copy
import operator


data = [int(x) for x in raw_data.split(",")]
ops = {
  1: operator.add,
  2: operator.mul
}


def run(noun, verb):

  mem = copy.deepcopy(data)
  
  mem[1] = noun
  mem[2] = verb

  for i in range(0, len(mem), 4):
    op = mem[i]

    if op == 99:
      break

    mem[mem[i + 3]] = ops[op](mem[mem[i + 1]], mem[mem[i + 2]])

  return mem[0]


def find(val):
  for i in range(100):
    for j in range(100):
      if run(i, j) == val:
        return i, j


print(run(12, 2))

noun, verb = find(19690720)
print(100 * noun + verb)

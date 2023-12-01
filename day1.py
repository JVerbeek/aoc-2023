def digit_map():  return {
                 "one": 1,
                 "two": 2,
                 "three": 3,
                 "four": 4,
                 "five": 5,
                 "six": 6,
                 "seven": 7,
                 "eight": 8,
                 "nine": 9}

import re

def filter(x):
    return [int(i) for i in x]

with open("inputs/day1") as f:
    inp = f.readlines()

answer = 0
for line in inp:
    dlist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dmap = digit_map()
    repl = []
    for digit in dlist:  #gruwelijk gruwelijk
        match = re.finditer(rf"{digit}", line)
        match2 = re.finditer(rf"{str(dmap[digit])}", line)
        for m in match:
            repl.append((m.start(), str(dmap[m.group(0)])))
        for m in match2:
            repl.append((m.start(), m.group(0)))
    repl = sorted(repl)
    answer += int(repl[0][1] + repl[-1][1])
print(answer)
import numpy as np
with open("inputs/day9") as f:
    lines = [list(map(int, l.split())) for l in f.readlines()]

def extrapolate(stack, right=True):
    bottom, rest = stack[0], stack[1:]
    for val in rest:
        bottom = val + bottom if right else val - bottom
    return bottom

vals = []
for line in lines:
    stack = [line[0]]
    differences = line
    while not np.all(differences == 0):
        differences = np.diff(np.array(differences))
        stack.append(differences[0])
    stack = stack [::-1]
    vals.append(extrapolate(stack, right=False))
print(sum(vals))
import numpy as np; from matplotlib import path; import matplotlib.pyplot as plt
with open("inputs/day10") as f:
    lines = [[symbol for symbol in line.strip()] for line in f.readlines()]

connector_map = {"S": [(1, 0), (-1, 0), (0, -1), (0, 1)],
                 "|": [(1, 0), (-1, 0)],
                 "-": [(0, -1), (0, 1)],
                 "L": [(-1, 0), (0, 1)],
                 "J": [(-1, 0), (0, -1)],
                 "7": [(1, 0), (0, -1)],
                 "F": [(1, 0), (0, 1)],
                 ".": [(0, 0), (0, 0)]}

def get_next(x, y):
    cmap = connector_map.get(lines[x][y])   # get all connecting bits
    connecting = []
    for (dx, dy) in cmap:    # for each connecting bit
        pos = x + dx, y + dy  # check position it goes to
        subcmap = connector_map.get(lines[x + dx][y + dy])  # for that position get what that maps to
        if tuple([sum(x) for x in zip(pos, subcmap[0])]) == (x, y) or \
            tuple([sum(x) for x in zip(pos, subcmap[1])]) == (x, y):   # if its the starting bit
            connecting.append((x+dx, y+dy))  # we found the next connection
    return connecting

#find start + two loop start points
for ind, line in enumerate(lines):
    if "S" in line:
        sx, sy = ind, line.index("S")   # get the position of S
        connections = get_next(sx, sy)

loop = [(sx, sy)]
loop.insert(0, connections[0])
loop.append(connections[1])

while not loop[0] == loop[-1]:   # python eats its tail
    left = [c for c in get_next(*loop[0]) if c not in loop][0]
    right = [c for c in get_next(*loop[-1]) if c not in loop][0]
    loop.insert(0, left), loop.append(right)
    
print(max(loop.index((sx, sy)), len(loop) - 1 - loop.index((sx, sy)) ))

points = 0
enclosed = []
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if (x, y) not in loop:
            cross = 0
            while y > 0:
                cross += (x, y) in loop and lines[x][y] in "JLS|"
                y -= 1
            points += cross % 2 == 1
print(points)

# alternatively, dirty solution
points = 0
ploop = path.Path(loop)
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if (x, y) not in loop and ploop.contains_point((x, y)):
            points += 1
print(points)

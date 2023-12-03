import math
total_cubes = {"red": 12, "green": 13, "blue": 14}

with open("inputs/day2") as f:
    inp = f.readlines()

part = 1
answer = 0
for line in inp:
    line = line.split(":")
    ident, game = line[0].split(" ")[1], line[1]
    for draw in game.split(";"):  # 3 red, 4 green...
        cubes = {cube.split(" ")[2].strip(): int(cube.split(" ")[1]) for cube in draw.split(",")}
        possible = all([(total_cubes[color]- cubes[color]) >= 0 for color in cubes.keys()])
        if not possible:
            ident = 0
    answer += int(ident)
print("Answer for 1 is", answer)

answer = 0
for line in inp:
    line = line.split(":")
    ident, game = line[0].split(" ")[1], line[1]
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for draw in game.split(";"):  # 3 red, 4 green...
        # for each draw see if its larger than current best
        cubes = {cube.split(" ")[2].strip(): int(cube.split(" ")[1]) for cube in draw.split(",")}
        for color, value in cubes.items():
            if max_cubes[color] <= value:
                max_cubes[color] = value
    
    answer += math.prod(list(max_cubes.values()))
print("Answer for 2 is", answer)
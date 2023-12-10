import math, time
with open("inputs/day6") as f:
    lines = f.readlines()
times = int("".join(lines[0].split()[1:]))
distances = int("".join(lines[1].split()[1:]))

def solutions(a, b, c):
    if b ** 2 > 4 * a * c: # make assumption that it has two roots 
        root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return int(root2 - root1)

def fast_win(game):
    return solutions(-1, game[0], -game[1])

start_time = time.time()
print(fast_win((times, distances)))
print("--- %s seconds ---" % (time.time() - start_time))
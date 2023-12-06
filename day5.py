import numpy as np
with open("inputs/day5") as f:
    input = f.readlines()

seeds = [int(i) for i in input[0].strip().split(" ")[1:]] 
pairs = []
for i in range(1, len(seeds), 2):
    pairs.append((seeds[i -1], seeds[i]))

blocks, block = [], []
for line in input[1:]:
    if "map" not in line and line != "\n":
        block.append(line.strip())
    elif "map" in line:
        blocks.append(block)
        block = []
blocks.append(block)

def make_map(seed, block):
    new_location = seed
    for line in block:
        dest, src, rng = (int(i) for i in line.strip().split(" "))
        if src + rng > seed >= src:
            new_location = dest + (seed - src)   # difference between seed and src is offset in dest
    return new_location

def make_range_map(start, stop, block):
    for line in block:
        rstart, rstop, r = (int(i) for i in line.strip().split(" ")) 

final_destination = []
for start, rng in pairs:
    batch = 10000
    loc_candidates = []
    print(rng/batch)
    for block in blocks:
        start = make_map(start, block)
        end = make_map(start + rng, block)
        print(start, end)
    final_destination.append(min(loc_candidates))
    print("finished seedpair")
print(final_destination)
    
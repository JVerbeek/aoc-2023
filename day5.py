import numpy as np
with open("inputs/test5") as f:
    input = f.readlines()

seeds = [int(i) for i in input[0].strip().split()[1:]] 
pairs = []
for i in range(1, len(seeds), 2):
    pairs.append((seeds[i - 1], seeds[i]))

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
        dest, src, rng = map(int, line.split(" "))
        if src + rng > seed >= src:
            new_location = dest + (seed - src)   # difference between seed and src is offset in dest
            break
    return new_location

final_destination = []
#  start  +++++++++++++++++++++++++ end
#  start         ns           ne      end
#  start   nss       nse  nes   nen    end  ---> find min left point
locs = []
seeds = [pair[0] for pair in pairs]
while seeds:
    seed = seeds.pop()
    for block in blocks:
        seed = make_map(seed, block)
    locs.append(seed)
    for block in blocks:
        for line in block:
            dest, src, rng = map(int, line.split(" "))
            
print(locs)
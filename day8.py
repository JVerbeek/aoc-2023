import time, math
with open("inputs/day8") as f:
    f = f.readlines()

instructions = list(map(int, f[0].replace("L", "0").replace("R", "1").strip()))
graph = [ve.split(" = ") for ve in f[2:]]
graph = [(p[0], p[1].strip("()\n").split(", ")) for p in graph]
graph = {node: edge for (node, edge) in graph}

nodes = list(filter(lambda v: v.endswith("A"), list(graph.keys()))) # replace "A" with "AAA" for part 1
sinks = set()
answer = 0
steps = 0
# Observation: all nodes that end in Z are sink nodes, meaning that each node i in range(len(nodes)) returns there after N_i iterations
# Finding all N_i and computing the least common multiple of that should give answer

while not answer: # d- d- d- danger zone
    for instruction in instructions:
        steps += 1
        nodes = list(map(lambda x: graph[x][instruction], nodes))
        reached_end = [sinks.add(steps) for n in nodes if n.endswith("Z")]  
    if len(sinks) == len(nodes):  # we have found all cycle times
        answer = math.lcm(*list(sinks))
print(answer)

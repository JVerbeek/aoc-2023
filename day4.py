import re
with open("inputs/day4") as f:
    card = f.readlines()

answer = 0
counter = {i: 1 for i in range(1, len(card)+1)}
for line in card:
    winning, mine = line.strip().split(" | ")
    linenumber = int(re.search(r"\s\d+", line).group(0))
    winning = set(winning.split(": ")[1].strip().split(" "))
    mine = set(mine.strip().split(" "))
    numbers = mine.intersection(winning)
    numbers.remove("") if "" in numbers else ""
    answer += 2 ** (len(numbers) - 1) if len(numbers) > 0 else 0
    for i in range(0, len(numbers)): # how many matching numbers
        counter[linenumber+i+1] += counter[linenumber]   # add counter value 
print(answer, sum(list(counter.values())))

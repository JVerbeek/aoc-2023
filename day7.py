import numpy as np; import time
with open("inputs/day7") as f:
    lines = f.readlines()

order = 'AKQT98765432J'[::-1]
types = list(range(7))[::-1]

def find_type(hand):
    hand = [h for h in hand]
    cards, counts = np.unique(hand, return_counts=True)

    if any(counts == 5): # 5oak, or if 4 or 5 jokers, 5oak
        t = types[0]
    elif any(counts == 4): # 4oak
        t = types[1]   # if one joker, 5oak, else, 4oak
    elif any(counts == 3):  # 3oak
        if any(counts == 2):   # full house
            t = types[2]
        else:
            t = types[3]  # else, its 3oak
    elif sum(counts == 2) == 2:  # two pair
        t = types[4]   # there can only be one joker which makes it fh
    elif sum(counts == 2) == 1:  # one pair
        t = types[5]
    elif all(counts == 1):   # all unique; joker makes one pair
        t = types[6]
    return t

hands = []
t = time.time()
for line in lines:
    hand, bid = line.strip().split()
    options = [hand.replace("J", sym) for sym in order[1:]]
    htypes = list(map(find_type, options))
    strength = [order.find(h) for h in hand]
    hands.append((max(htypes), strength, int(bid)))
print(sum([(r+1)*h[-1] for r, h in enumerate(sorted(hands))]), time.time() - t)
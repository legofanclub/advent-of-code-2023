# zip hands and bids
# sort by hand strength (by writing a comparison sort for hands)
# calculate total of winnings

# answer: 250757288

from collections import defaultdict
from functools import cmp_to_key

hands = []
bids = []

f = open("input.txt", "r")

for line in f:
    line = line.rstrip()
    hand, bid = line.split()
    hands.append(hand)
    bids.append(bid)

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

card_value = {}
for i, c in enumerate(reversed(cards)):
    card_value[c] = i

both = list(zip(hands, bids))

def handRank(h):
    d = defaultdict(int)
    jokers = 0
    for card in cards:
        d[card] = h.count(card)
    
    counts = [val for key, val in d.items() if val != 0 and key != "J"]
    counts.sort(reverse = True)

    jokers = d["J"]
    while jokers > 0 and len(counts) > 0:
        for i, x in enumerate(counts):
            while counts[i] < 5 and jokers > 0:
                counts[i] += 1
                jokers -= 1

    if len(counts) == 0:
        counts = [5]
    
    if len(counts) == 1:
        return 7 # 5 of a kind
    elif 4 in counts and 1 in counts:
        return 6 # 4 of a kind
    elif 3 in counts and 2 in counts:
        return 5 # full house
    elif 3 in counts and counts.count(1) == 2:
        return 4 # 3 of a kind
    elif counts.count(2) == 2 and 1 in counts:
        return 3 # 2 pair
    elif 2 in counts and counts.count(1) == 3:
        return 2 # 1 pair
    else:
        return 1 # high card

def tiebreak(h1, h2):
    for i in range(5):
        if card_value[h1[i]] > card_value[h2[i]]:
            return 1
        elif card_value[h1[i]] < card_value[h2[i]]:
            return -1
    return 0

def compare_hands(h1, h2):
    h1 = h1[0]
    h2 = h2[0]
    if handRank(h1) < handRank(h2):
        return -1
    elif handRank(h1) > handRank(h2):
        return 1
    else:
        return tiebreak(h1, h2)
    
result = 0
both.sort(key=cmp_to_key(compare_hands))
for i, (hand, bid) in enumerate(both, start = 1):
    result += int(bid)*i

print(result)
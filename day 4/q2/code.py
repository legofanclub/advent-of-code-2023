# use a hashmap to keep track of the number of copies required of each card
# multiply the results using the hashmap

# time complexity: O(n)
# space complexity: O(1)

from collections import defaultdict

with open("input.txt", "rb") as f:
    num_lines = sum(1 for _ in f)
f = open("input.txt", "r")

cardQuantity = defaultdict(lambda: 1)

total = 0
for i, line in enumerate(f):
    line = line[line.index(":") + 2:].rstrip().split("|")
    winners = set(line[0].split())
    seen = line[1].split()

    wins = len([x for x in seen if x in winners])

    if i not in cardQuantity:
            cardQuantity[i] = 1

    if wins > 0:
        for j in range(1, wins + 1):
            if i + j > num_lines:
                break
            cardQuantity[i+j] += cardQuantity[i]

print(sum([val for key, val in cardQuantity.items()]))
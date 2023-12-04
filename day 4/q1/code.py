# put winners in set and check if each number is a winner

# time complexity: O(n)
# space complexity: O(1)

f = open("input.txt", "r")

total = 0
for line in f:
    line = line[line.index(":") + 2:].rstrip().split("|")
    winners = set(line[0].split())
    seen = line[1].split()

    wins = len([x for x in seen if x in winners])
    if wins > 0:
        total += 2**(wins - 1)

print(total)
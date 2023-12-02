# read line by line and pick first and last number in each line

# time complexity: O(n)
# space complexity: O(1)

# answer: 54877

f = open("input.txt", "r")

ints = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

total = 0

for line in f:
    combo = []
    last = ""
    for c in line:
        if c in ints:
            if len(combo) == 0:
                combo.append(c)
            last = c
    combo.append(last)
    total += int("".join(combo))

print(total)
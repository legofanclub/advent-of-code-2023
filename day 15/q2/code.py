# hashing the letters in the input before the symbol gets the box number
# individual boxes are deques

# time complexity: O(n^2)
# space complexity: O(n)

# answer: 241094

from collections import defaultdict, deque

f = open("input.txt", "r")

data = []
data = f.readline().rstrip().split(",")

boxes = defaultdict(deque)

def hashFunc(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

for single in data:
    if "=" in single:
        label, fLength = single.split("=")
        box = boxes[hashFunc(label)]

        if label in [x[0] for x in box]:
            i = [x[0] for x in box].index(label)
            boxes[hashFunc(label)][i] = (label, fLength)
        else:
            boxes[hashFunc(label)].append((label, fLength))

    else: # - case
        label = single[:-1]
        box = boxes[hashFunc(label)]
        if label in [x[0] for x in box]:
            val = [x[0] for x in box].index(label)
            box.remove(box[val])

def calculatePower(boxes):
    total = 0
    for i, dq in boxes.items():
        for j, val in enumerate(dq, start = 1):
            total += (i + 1)*j*int(val[1])
    return total

print(calculatePower(boxes))
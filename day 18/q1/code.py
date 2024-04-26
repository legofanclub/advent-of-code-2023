# normalize coordinates to start at (0,0)
# plot on 2d array
# flood fill 2d array and count

# flood fill starting at (220, 183) and count all excavated tiles

# answer: 48652

import sys

f = open("input.txt", "r")

sys.setrecursionlimit(100000)

data = []
for line in f:
    direction, length = line.rstrip().split()[:2]
    data.append((direction, int(length)))

currCoords = (0,0)

dugCoords = [(0,0)]

dirToTup = {}

dirToTup["R"] = (0, 1)
dirToTup["L"] = (0, -1)
dirToTup["U"] = (-1, 0)
dirToTup["D"] = (1, 0)

def addTuple(tup1, tup2):
    return tuple([sum(x) for x in zip(tup1, tup2)])

for direction, length in data:
    for i in range(length):
        dugCoords.append(addTuple(dugCoords[-1], dirToTup[direction]))

# adjust mincoords to have smallest coords at 0
min_y = min([x[0] for x in dugCoords])
min_x = min([x[1] for x in dugCoords])

min_y *= -1
min_x *= -1

dugCoords = [(y + min_y, x + min_x) for y, x in dugCoords]

max_y = max([x[0] for x in dugCoords])
max_x = max([x[1] for x in dugCoords])

data = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]

for y, x in dugCoords:
    data[y][x] = "#"

# 220 y and 183x is inside loop
    
count = 0
def floodFill(y, x):
    # flood fills data with '#' and counts the number of filled tiles
    global count
    if data[y][x] != "#":
        count += 1
        data[y][x] = "#"
        floodFill(y-1, x)
        floodFill(y+1, x)
        floodFill(y, x-1)
        floodFill(y, x+1)

floodFill(220, 183)
print(count + len(dugCoords) - 1)
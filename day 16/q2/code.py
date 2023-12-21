# simulate the beams and track energized tiles in a 2d array

import sys

sys.setrecursionlimit(10000)
f = open("input.txt", "r")
layout = []

# answer: 8148

for line in f:
    layout.append(list(line.rstrip()))

energized = [[0 for _ in range(len(layout[0]))] for i in range(len(layout))]

def addTuple(tup1, tup2):
    return tuple([sum(x) for x in zip(tup1, tup2)])

def outOfBounds(location):
    return not (location[0] < len(layout) and location[0] >= 0 and location[1] < len(layout[0]) and location[1] >= 0)

seen = set()

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def simulateBeam(location, direction):

    asString = ",".join([str(x) for x in location]) + "and" + ",".join([str(x) for x in direction])
    if asString in seen:
        return
    else:
        seen.add(asString)

    y, x = location[0], location[1]

    if outOfBounds(location):
        return
    
    energized[y][x] = 1

    symbol = layout[y][x]

    match symbol:
        case ".":
            simulateBeam(addTuple(location, direction), direction)
        case "\\":
            if direction == right: # right to down
                    direction = down
            elif direction == left: # left to up
                    direction = up
            elif direction == down: # down to right
                    direction = right
            elif direction == up: # up to left
                    direction = left
            simulateBeam(addTuple(location, direction), direction)
        case "/":
            if direction == left: # left to down
                direction = down
            elif direction == right: # right to up
                direction = up
            elif direction == down: # down to left
                direction = left
            elif direction == up: # up to right
                direction = right
            simulateBeam(addTuple(location, direction), direction)
        case "|":
            if direction == right or direction == left:
                simulateBeam(addTuple(location, up), up)
                simulateBeam(addTuple(location, down), down)
            else:
                simulateBeam(addTuple(location, direction), direction)
        case "-":
            if direction == up or direction == down:
                simulateBeam(addTuple(location, left), left)
                simulateBeam(addTuple(location, right), right)
            else:
                simulateBeam(addTuple(location, direction), direction)



width = len(layout[0])
height = len(layout)

maximum = 0
def sumE(energized):
    return sum([sum(x) for x in energized])

for i in range(0, width): # top edge
    energized = [[0 for _ in range(len(layout[0]))] for i in range(len(layout))]
    seen = set()
    simulateBeam((0, i), down)
    maximum = max(sumE(energized), maximum)
for i in range(0, height): # left edge
    energized = [[0 for _ in range(len(layout[0]))] for i in range(len(layout))]
    seen = set()
    simulateBeam((i, 0), right)
    maximum = max(sumE(energized), maximum)
for i in range(0, width): # bottom edge
    energized = [[0 for _ in range(len(layout[0]))] for i in range(len(layout))]
    seen = set()
    simulateBeam((height - 1, i), up)
    maximum = max(sumE(energized), maximum)
for i in range(0, width): # right edge
    energized = [[0 for _ in range(len(layout[0]))] for i in range(len(layout))]
    seen = set()
    simulateBeam((i, width - 1), left)
    maximum = max(sumE(energized), maximum)

print(maximum)
# simulate the beams and track energized tiles in a 2d array

import sys

sys.setrecursionlimit(10000)
f = open("input.txt", "r")
layout = []

# answer: 7951

for line in f:
    layout.append(list(line.rstrip()))

energized = [[0 for _ in range(len(layout[0]))] for i in range(len(layout))]

def addTuple(tup1, tup2):
    return tuple([sum(x) for x in zip(tup1, tup2)])

def outOfBounds(location):
    return not (location[0] < len(layout) and location[0] >= 0 and location[1] < len(layout[0]) and location[1] >= 0)

seen = set()

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
            match direction:
                case (0, 1): # right to down
                    direction = (1,0)
                case (0, -1): # left to up
                    direction = (-1, 0)
                case (1, 0): # down to right
                    direction = (0, 1)
                case (-1, 0): # up to left
                    direction = (0, -1)
            simulateBeam(addTuple(location, direction), direction)
        case "/":
            match direction:
                case (0, -1): # left to down
                    direction = (1,0)
                case (0, 1): # right to up
                    direction = (-1, 0)
                case (1, 0): # down to left
                    direction = (0, -1)
                case (-1, 0): # up to right
                    direction = (0, 1)
            simulateBeam(addTuple(location, direction), direction)
        case "|":
            if direction == (0, 1) or direction == (0, -1):
                up = (-1, 0)
                down = (1, 0)
                simulateBeam(addTuple(location, up), up)
                simulateBeam(addTuple(location, down), down)
            else:
                simulateBeam(addTuple(location, direction), direction)
        case "-":
            if direction == (-1, 0) or direction == (1, 0):
                left = (0, -1)
                right = (0, 1)
                simulateBeam(addTuple(location, left), left)
                simulateBeam(addTuple(location, right), right)
            else:
                simulateBeam(addTuple(location, direction), direction)

simulateBeam((0,0), (0,1))

print(sum([sum(x) for x in energized]))
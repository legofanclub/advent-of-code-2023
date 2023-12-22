from functools import cache
import sys
sys.setrecursionlimit(10000)

# simulate with memoization and pruning

# answer: 1180
# 1 hour, 7 minutes, and 17 seconds

# bounding steps at 350 took 43 minutes and 52 seconds but produced a non-minimal answer: 1186

f = open("input.txt", "r")

lavaMap = []

for line in f:
    lavaMap.append([int(x) for x in line.rstrip()])

up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def inbounds(location):
    y, x = location[0], location[1]
    return x >= 0 and y >= 0 and x < len(lavaMap[0]) and y < len(lavaMap)

def addTuple(tup1, tup2):
    return tuple([sum(x) for x in zip(tup1, tup2)])

def lRelCurDir(direction):
    if direction == up:
        return left
    elif direction == left:
        return down
    elif direction == down:
        return right
    elif direction == right:
        return up
    
def rRelCurDir(direction):
    if direction == up:
        return right
    elif direction == right:
        return down
    elif direction == down:
        return left
    elif direction == left:
        return up

@cache
def bestPath(location, direction, lineLength, steps):

    # base cases
    if not inbounds(location) or lineLength > 10 or steps > 400:
        return float('inf')

    y, x = location[0], location[1]
    curNum = lavaMap[y][x]
    if location == (len(lavaMap) - 1, len(lavaMap[0]) - 1) and lineLength >= 4:
        return curNum

    # can go left, right or straight, but not backwards
    leftPath = rightPath = straightPath = float('inf')

    lRc = lRelCurDir(direction)
    rRc = rRelCurDir(direction)

    if lineLength < 4:
        straightPath = bestPath(addTuple(location, direction), direction, lineLength + 1, steps + 1)
        return straightPath + curNum
    else:
        leftPath = bestPath(addTuple(location, lRc), lRc, 1, steps + 1)
        rightPath = bestPath(addTuple(location, rRc), rRc, 1, steps + 1)
        straightPath = bestPath(addTuple(location, direction), direction, lineLength + 1, steps + 1)

    return min(leftPath, rightPath, straightPath) + curNum

print(min(bestPath((0,1), right, 1, 0), bestPath((1,0), down, 1, 0)))
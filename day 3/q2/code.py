from functools import cache

# find total of products of all pairs of numbers joined by 1 star

# gear is a star adjacent to exactly 2 numbers

# for each star, find all numbers adjacent
# if there are exactly 2, multiply them and add to total

# time complexity: O(n)
# space complexity: O(n)

f = open("input.txt", "r")

a = []
# convert input to 2d array
for line in f:
    l = []
    for c in line:
        if c != '\n':
            l.append(c)
    a.append(l)

indexToNum = {}
def getNum(i: int, j: int) -> int | None:
    # check cache ## todo
    if (i, j) in indexToNum:
        return indexToNum[(i,j)]

    if not a[i][j].isdigit():
        return None

    # go backwards and forwards to get whole num
    lo = j - 1
    while lo >= 0 and a[i][lo].isdigit():
        lo -= 1
    lo += 1

    hi = j + 1
    while hi < len(a[0]) and a[i][hi].isdigit():
        hi += 1
    
    num = int("".join(a[i][lo:hi]))

    # put all positions in dict with num value as value
    for k in range(lo, hi):
        indexToNum[(i, k)] = num
    
    return num



def allNumsAdjacent(i: int, j: int) -> list[int]:
    res = []
    up = False
    down = False
    if i > 0:               # up
        n = getNum(i-1,j)
        if n != None:
            res.append(n)
            up = True
    if j > 0:               # left
        n = getNum(i,j-1)
        if n != None:
            res.append(n)
    if i > 0 and j > 0 and not up:    # diagonal up left
        n = getNum(i-1,j-1)
        if n != None:
            res.append(n)
    if i < len(a) - 1:      # down
        n = getNum(i+1,j)
        if n != None:
            res.append(n)
            down = True
    if j < len(a[0]) - 1:   # right
        n = getNum(i,j+1)
        if n != None:
            res.append(n)
    if i < len(a) - 1 and j < len(a[0]) - 1 and not down: # diagonal down right
        n = getNum(i+1,j+1)
        if n != None:
            res.append(n)
    if i > 0 and j < len(a[0]) - 1 and not up:    # diagonal up right
        n = getNum(i-1,j+1)
        if n != None:
            res.append(n)
    if i < len(a) - 1 and j > 0 and not down:       # diagonal down left
        n = getNum(i+1,j-1)
        if n != None:
            res.append(n)

    return res

# find all gears and multiply nums adjacent if there are exactly 2 of them
total = 0
for i, line in enumerate(a):
    for j, c in enumerate(line):
        if c == "*":
            l = allNumsAdjacent(i,j)
            if len(l) == 2:
                total += l[0]*l[1]

print(f"result: {total}")
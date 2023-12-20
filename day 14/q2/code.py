# tilt all rocks north, repeat for each cardinal direction
# simulate and detect cycles, calculate answer once cycle has been detected
# calculate the total load: sum of distances of rocks from south

# hashmap approach for cycle detection taken from tildes answer

# answer: 94255

matrix = []
f = open("input.txt", "r")

for line in f:
    matrix.append(line.rstrip())

def calculateLoad(matrix):
    total = 0
    for i, line in enumerate(reversed(matrix), start = 1):
        total += i*line.count("O")
    return total

def moveRockColumn(column):
    lastRock = -1
    numRocks = 0
    res = []
    for i, v in enumerate(column):
        if v == "#":
            prevLastRock = lastRock
            lastRock = i
            for j in range(prevLastRock, lastRock-1):
                if numRocks > 0:
                    res.append("O")
                else:
                    res.append(".")
                numRocks -= 1
            res.append("#")
            numRocks = 0
        elif v == "O":
            numRocks += 1
    
    # edge
    for j in range(lastRock, len(column) - 1):
        if numRocks > 0:
            res.append("O")
        else:
            res.append(".")
        numRocks -= 1
    numRocks = 0
    
    return "".join(res)        

def moveRocks(matrix):
    # moves all rocks in the matrix
    res = []
    for column in list(zip(*matrix)):
        new_column = moveRockColumn(column)
        res.append(new_column)
    return list(zip(*res))       

def display(matrix):
    for line in matrix:
        print("".join(line))
    print("\n")

def spinCycle(matrix):
    matrix = moveRocks(matrix)
    matrix = moveRocks(zip(*matrix[::-1]))
    matrix = moveRocks(zip(*matrix[::-1]))
    matrix = moveRocks(zip(*matrix[::-1]))
    matrix = zip(*matrix[::-1])
    return list(matrix)


seen = {}
countdown = False
for i in range(1000000000):
    matrix = spinCycle(matrix)
    asString = "".join(["".join(line) for line in matrix])

    if countdown:
        c -= 1
        if c == 0:
            break

    # check for a loop
    if asString in seen:
        print(f'current i: {i}, prev i: {seen[asString]}')
        c = (1000000000 - seen[asString]) % (i - seen[asString]) - 1 # number in sequence that final tilt is (0 indexed)
        countdown = True
    seen[asString] = i

matrix = list(matrix)    
print(calculateLoad(matrix))
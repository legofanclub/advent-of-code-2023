# tilt all rocks north
# calculate the total load: sum of distances of rocks from south

# rocks are blocked by other rocks and by #
# move rocks column by column

# answer: 113078

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

matrix = moveRocks(matrix)

print(calculateLoad(matrix))
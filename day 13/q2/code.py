# search each line for all reflections
# choose the reflection that is contained in all lines
# to do vertical, first transpose the matrix
# count for one imperfection

# answer: 34230

# time complexity: O(n*m^2)
# space complexity: O(m)
# n is the number of cases and m is the longest dimension of an individual case

f = open("input.txt", "r")

matrices = []
cur = []
for line in f:
    if line == "\n":
        matrices.append(cur)
        cur = []
    else:
        cur.append(list(line.rstrip()))
matrices.append(cur)

def reflectionIndex(matrix):
    # returns the index of horizontal line of reflection in matrix
    # worst case: O(n^2)

    d = {}
    for i, line in enumerate(matrix):
        d[i] = hash(tuple(line))

    def checkRadiatingOutwards(i, j):
        smudge = False
        for i, j in zip(range(i, -1, -1), range(j, len(matrix))):
            if d[i] != d[j]:
                if smudge:
                    return False
                else:
                    for x in range(len(matrix[0])):
                        if matrix[i][x] != matrix[j][x]:
                            if not smudge:
                                smudge = True
                            else:
                                return False
        return smudge

    for i, j in zip(range(0, len(matrix) - 1), range(1, len(matrix))):
        # if d[i] == d[j]:
        if checkRadiatingOutwards(i, j):
            return i

def rotate(matrix):
    rotated = list(zip(*matrix[::-1]))
    return rotated

def reflectionNum(matrix):
    i = reflectionIndex(matrix)
    if i == None:
        i = reflectionIndex(rotate(matrix)) + 1
    else:
        i = (i+1) * 100 # i is a horizontal line
    return i

print(sum([reflectionNum(matrix) for matrix in matrices]))
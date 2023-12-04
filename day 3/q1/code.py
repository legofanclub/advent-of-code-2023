# look through 2d array and check if each number is adjacent to a symbol
# time complexity: O(n)
# space complexity: O(n)

f = open("input.txt", "r")

a = []

symbols = set(["!", "@", "#", "$", "%", "^", "&", "*", "-", "+", "=", "/"])

# convert input to 2d array
for line in f:
    l = []
    for c in line:
        if c != '\n':
            l.append(c)
    a.append(l)

def symbolClose(i,j):
    res = False
    if a[i][j] in symbols:
        res = True
    if i > 0:
        res = res or a[i-1][j] in symbols
    if j > 0:
        res = res or a[i][j-1] in symbols
    if i > 0 and j > 0:
        res = res or a[i-1][j-1] in symbols
    if i < len(a) - 1:
        res = res or a[i+1][j] in symbols
    if j < len(a[0]) - 1:
        res = res or a[i][j+1] in symbols
    if i < len(a) - 1 and j < len(a[0]) - 1:
        res = res or a[i+1][j+1] in symbols
    if i > 0 and j < len(a[0]) - 1:
        res = res or a[i-1][j+1] in symbols
    if i < len(a) - 1 and j > 0:
        res = res or a[i+1][j-1] in symbols

    return res


total = 0
for i, line in enumerate(a):
    current = []
    for j, c in enumerate(line):

        if c == "." or c in symbols:
            # end current
            if len(current) > 0:
                if symbolAdjacent:
                    total += int("".join(current))
                current = []
                symbolAdjacent = False

        else: # c is an integer
            # check above and below
            symbolAdjacent = (len(current) > 0 and symbolAdjacent) or symbolClose(i,j)
            current.append(c)
        
        if j == len(line) - 1:
            # end current
            if len(current) > 0:
                if symbolAdjacent:
                    total += int("".join(current))
                current = []
                symbolAdjacent = False

print(total)
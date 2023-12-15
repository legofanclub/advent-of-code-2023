# steps is length of loop // 2
# dfs the pipe until you reach s again

# time complexity: O(n)
# space complexity: O(n) for stack

# answer: 6778

import sys

sys.setrecursionlimit(1000000)
f = open("input.txt", "r")
cur = []
pipes = []
for i, line in enumerate(f):
    if "S" in line:
        cur = [i, line.index("S")]
        line = line.replace("S", "-") # hack based on input
    pipes.append(list(line.rstrip()))

move = {}
#             y  x    y  x
move["|"] = [(1, 0), (-1, 0)]
move["-"] = [(0, 1), (0, -1)]
move["L"] = [(0, 1), (-1, 0)]
move["J"] = [(0, -1), (-1, 0)]
move["7"] = [(0, -1), (1, 0)]
move["F"] = [(0, 1), (1, 0)]

def search(cur, prev, dist, seen):
    if cur == original and seen:
        return dist
    
    # search through possible moves to move forward
    symbol = pipes[cur[0]][cur[1]]
    next = prev.copy()
    i = 0
    while next == prev:
        next = [cur[0] + move[symbol][i][0], cur[1] + move[symbol][i][1]]
        i += 1

    return search(next, cur, dist + 1, True)

# print(pipes)
original = cur
print(search(cur, [-1,-1], 0, False)//2)
# steps is length of loop // 2
# dfs the pipe until you reach s again
# use map of pipe and count tiles enclosed in each line horizontally (ray casting algorithm)

# looked up how to handle case where line is flat

# time complexity: O(n)
# space complexity: O(n) for stack

# answer: 433

import sys

sys.setrecursionlimit(1000000)
f = open("input.txt", "r")
cur = []
pipes = []
for i, line in enumerate(f):
    if "S" in line:
        cur = [i, line.index("S")]
        line = line.replace("S", "-") # hack, s has to be replaced manually based on input
    pipes.append(list(line.rstrip()))

pipes_only = [[None] * len(pipes[0]) for _ in range(len(pipes))]

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
    pipes_only[cur[0]][cur[1]] = symbol
        
    next = prev.copy()
    i = 0
    while next == prev:
        next = [cur[0] + move[symbol][i][0], cur[1] + move[symbol][i][1]]
        i += 1

    return search(next, cur, dist + 1, True)

original = cur
search(cur, [-1,-1], 0, False)//2

enclosed = [[0] * len(pipes[0]) for _ in range(len(pipes))]

total = 0
for i, line in enumerate(pipes_only):
    last_turn = None
    on = False
    for j, symbol in enumerate(line):
        if symbol == "L" or symbol == "F":
            last_turn = symbol
        elif symbol == "7":
            if last_turn == "L":
                on = not on
            last_turn = symbol
        elif symbol == "J":
            if last_turn == "F":
                on = not on
            last_turn = symbol
        elif symbol == "|":
            on = not on
        elif on and not symbol:
            total += 1
            enclosed[i][j] = 1

print(total)
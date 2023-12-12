# simulate

# checked forum after wrong answer
# found that numpy lcm gave different answer to math.lcm
# this solution is not general to the problem as written
# answer: 14449445933179

import math


f = open("input.txt", "r")
instructions = list(f.readline().rstrip())

curs = []
cur_to_left_right = {}
f.readline() # skip blank line
for line in f:
    cur, left, right = line[0:3], line[7:10], line[12:15]
    cur_to_left_right[cur] = (left, right)
    if cur[-1] == "A":
        curs.append(cur)

times = []
for cur in curs:
    steps = 0
    while cur[-1] != "Z":
        cur = cur_to_left_right[cur]
        direction = instructions[steps % len(instructions)]
        if direction == "L":
            cur = cur[0]
        else:
            cur = cur[1]
        steps += 1
    times.append(steps)

print("lowest common multiple: ", math.lcm(*times))
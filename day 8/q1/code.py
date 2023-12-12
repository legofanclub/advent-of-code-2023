# simulate

# answer: 18023

f = open("input.txt", "r")
instructions = list(f.readline().rstrip())

cur_to_left_right = {}
f.readline() # skip blank line
for line in f:
    cur, left, right = line[0:3], line[7:10], line[12:15]
    cur_to_left_right[cur] = (left, right)

steps = 0
cur = "AAA"
while cur != "ZZZ":
    cur = cur_to_left_right[cur]
    direction = instructions[steps % len(instructions)]
    if direction == "L":
        cur = cur[0]
    else:
        cur = cur[1]
    steps += 1

print(steps)
# iterate though games calcultating minimum required cubes in each

# time complexity: O(n)
# space complexity: O(1)

import operator
import functools

f = open("input.txt", "r")

res = 0

for game_index, line in enumerate(f, start = 1):
    line = line[line.index(":") + 2:]
    line = line.split(";")
    good = True

    minimums = {"red": 0, "green": 0, "blue": 0}

    for reveal in line:
        individual_reveals = reveal.split(",")
        seen = {"red": 0, "green": 0, "blue": 0}
        for single in individual_reveals:
            amount, color = single.split()
            seen[color] += int(amount)

        for color, amount in seen.items():
            minimums[color] = max(minimums[color], amount)
    
    if good:
        res += functools.reduce(operator.mul, [x for _, x in minimums.items()], 1)

print(res)

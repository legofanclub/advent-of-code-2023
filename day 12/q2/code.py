# try all combinations and check + memoization

# read online explanation when stuck
# use a memoized recursive function with pruning
# runtime: 33 seconds

# answer: 30568243604962

from functools import cache

def numWays(record, info):
    string = record
    expected_streaks = info

    @cache
    def recursive(index, lcs, prev_streaks):
        nonlocal string
        nonlocal expected_streaks
        # base case
        if index >= len(string):
            if lcs > 0:
                prev_streaks += tuple([lcs])
            
            if prev_streaks == expected_streaks:
                return 1
            else:
                return 0
            
        # pruning
        if len(prev_streaks) > len(expected_streaks):
            return 0
        for i, val in enumerate(prev_streaks[:-1]):
            if val != expected_streaks[i]:
                return(0)

        if string[index] == "?":
            if lcs > 0:
                dot_case = recursive(index + 1, 0, prev_streaks + tuple([lcs]))
            else:
                dot_case = recursive(index + 1, 0, prev_streaks)

            hashtag_case = recursive(index + 1, lcs + 1, prev_streaks)

            return dot_case + hashtag_case
        elif string[index] == ".":
            if lcs > 0:
                dot_case = recursive(index + 1, 0, prev_streaks + tuple([lcs]))
            else:
                dot_case = recursive(index + 1, 0, prev_streaks)
            return dot_case
        elif string[index] == "#":
            return recursive(index + 1, lcs + 1, prev_streaks)


    return recursive(0, 0, ())

# parse input
f = open("input.txt", "r")
data = []
for line in f:
    first, second = line.rstrip().split()
    first = list(first)
    first.append("?")
    first = (first * 5)[:-1]
    second = [int(x) for x in second.split(",")]
    second = second * 5
    data.append(("".join(first), tuple(second)))

total = 0
for record, info in data:
    total += numWays(record, info)

print(total)
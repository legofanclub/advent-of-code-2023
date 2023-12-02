# read line by line and pick first and last number in each line

# time complexity: O(n)
# space complexity: O(1)

# answer: 54100

f = open("input.txt", "r")

ints = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0

for line in f:

    combo = []
    last = ""
    for i, c in enumerate(line):
        if c in ints:
            if len(combo) == 0:
                combo.append(c)
            last = c
        
        # first character matches a number
        elif c in [x[0] for x in numbers]:
            for j, n in enumerate(numbers):
                if i+len(n) <= len(line):
                    if line[i:i+len(n)] == n:
                        if len(combo) == 0:
                            combo.append(str(j))
                        last = str(j)
        
    combo.append(last)
    total += int("".join(combo))

print(total)
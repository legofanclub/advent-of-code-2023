from itertools import pairwise

# simulate

# time complexity: O(n^2)
# space complexity: O(n^2)
# n is line length

f = open("input.txt", "r")

def predict(nums):
    if not all([x == 0 for x in nums]):
        lower = [y - x for x, y in pairwise(nums)]
        return nums[0] - predict(lower)
    else:
        return 0

total = 0
for line in f:
    total += predict([int(x) for x in line.split()])

print(total)
# perform HASH on input

# time complexity: O(n)
# space complexity: O(n)

# answer: 501680

f = open("input.txt", "r")

data = []
data = f.readline().rstrip().split(",")

def hashFunc(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur

total = 0
for val in data:
    total += hashFunc(val)

print(total)
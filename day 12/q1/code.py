# try all combinations and check

# read online explanation when stuck

# time complexity: O(2^n)
# space complexity: O(n) for stack
# n is maximum line length

# answer: 7407

f = open("input.txt", "r")

data = []

def correct(record, info):
    # returns True if the record matches info
    record = "".join(record)
    record = record.split(".")
    record = [x for x in record if len(x) > 0]
    counts = [len(x) for x in record]
    return counts == info

def numThatWork(record, info, built, i):
    if len(built) == len(record):
        if correct(built, info):
            return 1
        else:
            return 0
    
    if record[i] == "?":
        good = built.copy() + ["."]
        bad = built.copy() + ["#"]
        return numThatWork(record, info, good, i + 1) + numThatWork(record, info, bad, i + 1)
    else:
        built.append(record[i])
        return numThatWork(record, info, built, i + 1)
        
for line in f:
    first, second = line.rstrip().split()
    second = [int(x) for x in second.split(",")]
    data.append((first, second))

total = 0
for record, info in data:
    total += numThatWork(record, info, [], 0)

print(total)
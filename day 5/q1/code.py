# try every seed map against the incoming number

# time complexity: O(n)
# space complexity: O(n)

# parse the input
f = open("input.txt", "r")

class SeedMapLine():
    def __init__(self, sources):
        self.dest_range_start = int(sources[0])
        self.source_range_start = int(sources[1])
        self.range_length = int(sources[2])
    
    def convert(self, input: int) -> int:
        input = int(input)
        output = 0
        if input >= self.source_range_start and input < self.source_range_start + self.range_length:
            return self.dest_range_start + (input - self.source_range_start)
        else:
            return None

seeds = []
firstLine = f.readline()
seeds = firstLine[firstLine.index(":")+2:].split()

sts = set()
stf = set()
ftw = set()
wtl = set()
ltt = set()
tth = set()
htl = set()

maps = [sts, stf, ftw, wtl, ltt, tth, htl]

def addToMap(f, line, m):
    # skip the first line (which is text)
    while (line := f.readline()) and line != "\n":
        sources = line.rstrip()
        m.add(SeedMapLine(sources.split()))

while (line := f.readline()):
    if "seed-to-soil map:" in line:
        addToMap(f, line, sts)
    elif "soil-to-fertilizer map:" in line:
        addToMap(f, line, stf)
    elif "fertilizer-to-water map:" in line:
        addToMap(f, line, ftw)
    elif "water-to-light map:" in line:
        addToMap(f, line, wtl)
    elif "light-to-temperature map:" in line:
        addToMap(f, line, ltt)
    elif "temperature-to-humidity map:" in line:
        addToMap(f, line, tth)
    elif "humidity-to-location map:" in line:
        addToMap(f, line, htl)

def getLocationNumber(seed: int) -> int:
    num = seed
    for m in maps:
        for elem in m:
            t = elem.convert(num)
            if t != None:
                num = t
                break
    return num 

res = float('inf')
for seed in seeds:
    res = min(res, getLocationNumber(seed))


print(res)
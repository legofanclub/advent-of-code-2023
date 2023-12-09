# go backwards checking the lowest locations first
# approach taken from online

# time complexity: O(n)
# space complexity: O(n)

# took 4 minutes 57 seconds to run

# answer: 26714516

# parse the input
f = open("input.txt", "r")

class SeedMapLine():
    def __init__(self, sources):
        self.dest_range_start = int(sources[0])
        self.source_range_start = int(sources[1])
        self.range_length = int(sources[2])
    
    def convert(self, input: int) -> int:
        input = int(input)
        if input >= self.source_range_start and input < self.source_range_start + self.range_length:
            return self.dest_range_start + (input - self.source_range_start)
        else:
            return None
    
    def convert_backwards(self, input: int) -> int:
        input = int(input)
        if input >= self.dest_range_start and input < self.dest_range_start + self.range_length:
            return self.source_range_start + (input - self.dest_range_start)
        else:
            return None

seeds = []
firstLine = f.readline()
seeds = firstLine[firstLine.index(":")+2:].split()
seeds = [int(x) for x in seeds]

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

def contained_within(num, ranges):
    for start, length in ranges:
        if num >= start and num < start + length:
            return True
    return False

pairs = list(zip(seeds[::2], seeds[1::2]))
res = float('inf')
i = 0

def getSeedNumber(location: int) -> int:
    num = location
    for m in reversed(maps):
        for elem in m:
            t = elem.convert_backwards(num)
            if t != None:
                num = t
                break
    return num 

for possible_loc in range(10000000000):
    if contained_within(getSeedNumber(possible_loc), pairs):
        print(f"seed is: {getSeedNumber(possible_loc)}, location is: {possible_loc}")
        break
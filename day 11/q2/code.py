# check distance between all pairs

# time complexity: O(n^2)
# space complexity: O(n)

# answer: 904633799472

f = open("input.txt", "r")

all_galaxies = []

full_map = []

for line in f:
    full_map.append(list(line.rstrip()))

empty_columns = set()
for i in range(len(full_map[0])):
    seen = False
    for j in range(len(full_map)):
        if full_map[j][i] == "#":
            seen = True
            break
    if not seen:
        empty_columns.add(i)

i = 0
for line in full_map:
    if "#" not in line:
        i += 1000000 - 1
    else:
        j = j_original = 0
        for c in line:
            if c == "#":
                all_galaxies.append((i,j))
            elif j_original in empty_columns:
                j += 1000000 - 1
            j += 1
            j_original += 1
    i += 1

total = 0
for i, (init_y, init_x) in enumerate(all_galaxies[:-1]): # bug only finding closest to each galaxy, need to find all pairs
    for test_y, test_x in all_galaxies[i+1:]:
        min_dist = abs(init_y - test_y) + abs(init_x - test_x)
        total += min_dist
print(total)
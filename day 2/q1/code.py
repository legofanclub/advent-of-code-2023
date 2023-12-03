# check if each game has too many cubes in each draw

# time complexity: O(n)
# space complexity: O(1)

f = open("input.txt", "r")

expected = {"red": 12, "green": 13, "blue": 14}
res = 0

for game_index, line in enumerate(f, start = 1):
    line = line[line.index(":") + 2:]
    line = line.split(";")
    good = True

    for reveal in line:
        individual_reveals = reveal.split(",")
        seen = {"red": 0, "green": 0, "blue": 0}
        for single in individual_reveals:
            amount, color = single.split()
            seen[color] += int(amount)
        
        for color, amount in seen.items():
            if amount > expected[color]:
                good = False
                break
        
    if good:
        res += game_index

print(res)

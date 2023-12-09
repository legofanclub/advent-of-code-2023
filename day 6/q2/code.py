# concatenate all numbers together and simulate race

# time complexity: O(n)
# space complexity: O(1)

# answer: 34655848

f = open("input.txt", "r")

times = f.readline()
times = times[times.index(":")+1:]
times = times.lstrip()
times = times.split()

distances = f.readline()
distances = distances[distances.index(":")+1:]
distances = distances.lstrip()
distances = distances.split()

races = [(int("".join(times)), int("".join(distances)))]
print(races)

result = 0
for time, distance in races:
    ways = 0
    for i in range(0, time + 1):
        speed = i
        if (time - i)*speed > distance:
            ways += 1
    result += ways

print(result)
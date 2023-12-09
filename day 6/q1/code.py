# simulate races

# time complexity: O(n)
# space complexity: O(1)

# answer: 588588

f = open("input.txt", "r")

times = f.readline()
times = times[times.index(":")+1:]
times = times.lstrip()
times = times.split()

distances = f.readline()
distances = distances[distances.index(":")+1:]
distances = distances.lstrip()
distances = distances.split()

races = zip([int(x) for x in times], [int(x) for x in distances])

result = 1
for time, distance in races:
    ways = 0
    for i in range(0, time + 1):
        speed = i
        if (time - i)*speed > distance:
            ways += 1
    result *= ways

print(result)
# stole from here: https://elixirforum.com/t/advent-of-code-2023-day-18/60436/11

# get verticies of loop
# use shoelace formula on points to get area
# add to half perimeter + 1 (basically convert using pick's theorum)

# answer: 45757884535661


def assert_equals(actual, expected):
    assert actual == expected, f"Assertion failed: expected {expected}, got {actual}"


def decode(hex_code):
    dist_code = hex_code[:5]
    direction_code = hex_code[-1]

    direction_code_to_direction = {"0": "R", "1": "D", "2": "L", "3": "U"}

    return direction_code_to_direction[direction_code], int(dist_code, 16)


def get_instructions(file):
    instructions = []
    for line in file:
        hex_code_with_parens = line.rstrip().split()[-1]
        hex_code = hex_code_with_parens[2:-1]
        direction, distance = decode(hex_code)
        instructions.append((direction, distance))
    return instructions


def get_vertices(instructions):
    vertices = [(0,0)]
    current_pos = (0, 0)

    direction_to_tuple = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }

    for direction, distance in instructions:
        direction = direction_to_tuple[direction]
        current_pos = (direction[0]*distance + current_pos[0], direction[1]*distance + current_pos[1])
        vertices.append(current_pos)

    return(vertices)

def get_area(vertices):
    # use Shoelace formula
    ## turn vertices into a 'loop' loosely
    vertices.append(vertices[0])
    vertices.insert(0, vertices[-2])
    ## account for 'loopness' by changing range
    area = 0.5 * sum((vertices[i][1]*(vertices[i-1][0]-vertices[i+1][0]) for i in range(1, len(vertices)-1)))
    ## could be negative if loop goes clockwise
    area = abs(area)
    return area

def get_perimeter(vertices):
    perimeter = 0
    last_vert = vertices[0]
    for vert in vertices[1:]:
        distance = abs(vert[0] - last_vert[0]) + abs(vert[1] - last_vert[1])
        perimeter += distance
        last_vert = vert
    
    ## handle connection between vertices[-1] and vertices[0]
    last_vert = vertices[-1]
    vert = vertices[0]
    distance = abs(vert[0] - last_vert[0]) + abs(vert[1] - last_vert[1])
    perimeter += distance

    return perimeter


def solve(file) -> int:
    instructions = get_instructions(file)
    vertices = get_vertices(instructions)
    area = get_area(vertices)
    half_perimeter_plus_one = get_perimeter(vertices)/2 + 1
    return area + half_perimeter_plus_one


example_file = open("example.txt", "r")
assert_equals(decode("70c710"), ("R", 461937))
assert_equals(solve(example_file), 952408144115)
puzzle_input = open("puzzle_input.txt", "r")
print(f"answer to puzzle input is: {int(solve(puzzle_input))}")

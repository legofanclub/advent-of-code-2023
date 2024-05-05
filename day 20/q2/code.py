# find least common multiple of all inputs heading to kc which heads to rx
# used hints from online one website used was here: https://elixirforum.com/t/advent-of-code-2023-day-20/60474/4

# answer: 244151741342687

from collections import deque
import pprint

def assert_equals(actual, expected):
    assert actual == expected, f"Assertion failed: expected {expected}, got {actual}"

def get_name_to_func(input):
    name_to_func = {}
    for line in input:
        inp, out = [l.strip() for l in line.split("->")]
        if inp != "broadcaster":
            type = inp[0]
            name_to_func[inp[1:]] = {"type": type, "outputs": [o.strip() for o in out.split(",")], "inputs": [], "memory": 0}
        else:
            name_to_func[inp] = {"type": inp, "outputs": [o.strip() for o in out.split(",")], "inputs": [], "memory": 0}
    
    for name in name_to_func.keys():
        for name2 in name_to_func[name]["outputs"]:
            if name2 in name_to_func:
                name_to_func[name2]["inputs"].append(name)

    for name in name_to_func.keys():
        name_to_func[name]["input_memory"] = {key: 0 for key in name_to_func[name]["inputs"]}
    return name_to_func

def solve(input):
    name_to_func = get_name_to_func(input)
    high = 0
    low = 0
    cycle = 1
    for _ in range(100000000):
        queue = deque([('broadcaster', 0, None)])
        num_hi_pulses = 0
        num_lo_pulses = 0
        while queue:
            name, pulse, prev = queue.popleft()
            if name not in name_to_func:
                continue
            func = name_to_func[name]
            type = func["type"]
            outputs = func["outputs"]
            memory = func["memory"]

            if type == "%":
                if pulse == 1:
                    continue
                elif pulse == 0:
                    if memory == 0:
                        name_to_func[name]["memory"] = 1
                        pulse = 1
                    elif memory == 1:
                        name_to_func[name]["memory"] = 0
                        pulse = 0
            elif type == "&":
                name_to_func[name]["input_memory"][prev] = pulse
                if all([x == 1 for x in name_to_func[name]["input_memory"].values()]):
                    pulse = 0
                else:
                    pulse = 1
                    if name == "ph" or name == "vn" or name == "kt" or name == "hn":
                        print(f"{name} sent 1 pulse to kc at cycle {cycle}")
            elif type == "broadcaster":
                None
            else:
                raise Exception("this code block shouldn't be reached")

            # propagate pulses and update sums
            queue.extend([(next_name, pulse, name) for next_name in outputs])
            if pulse == 0:
                num_lo_pulses += len(outputs)
            else:
                num_hi_pulses += len(outputs)
        cycle += 1

puzzle_input = open("../puzzle_input.txt", "r")
print(f"answer to puzzle input is: {solve(puzzle_input)}")
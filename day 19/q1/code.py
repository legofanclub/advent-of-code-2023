# evaluate functions on each part

# answer: 480738

def assert_equals(actual, expected):
    assert actual == expected, f"Assertion failed: expected {expected}, got {actual}"

def functions_string_to_list(f_string):
    list_of_functions = []
    commands = f_string.split(",")
    for command in commands[:-1]:
        condition, body = command.split(":")
        list_of_functions.append((condition, body))
    list_of_functions.append((True, commands[-1]))
    return list_of_functions

def get_functions_dict(raw_functions):
    functions = {}
    for line in raw_functions:
        name, f = line.split("{")
        functions[name] = functions_string_to_list(f[:-1])
    return functions

def get_raw_data(file):
    raw_functions = []
    for line in file:
        if line == "\n":
            break
        raw_functions.append(line.rstrip())
    
    raw_values = []
    for line in file:
        raw_values.append(line.rstrip())
    
    return raw_functions, raw_values

def values_to_dict(raw_values):
    values = []
    for value in raw_values:
        value = value.replace("=", ":").replace("{", '{"').replace(":", '":').replace(",", ',"')
        values.append(eval(value))
    return values

def eval_function(func, value, functions):
    for condition, body in func:
        if condition == True or eval(condition, None, value):
            if body == "A":
                return True
            elif body == "R":
                return False
            else:
                return eval_function(functions[body], value, functions)
    raise NotImplementedError("code evaluation should not reach this point")

def accepted(functions, value):
    return eval_function(functions["in"], value, functions)
        
def get_accepted_values(functions, values):
    return [value for value in values if accepted(functions, value)]
    

def solve(file):
    raw_functions, raw_values = get_raw_data(file)
    functions = get_functions_dict(raw_functions) # name: [list of (condition, body)]
    values = values_to_dict(raw_values)
    accepted_values = get_accepted_values(functions, values)
    return sum([v['x'] + v['m'] + v['a'] + v['s'] for v in accepted_values])


sample_input = open("../sample_input.txt", "r")
assert_equals(solve(sample_input), 19114)
puzzle_input = open("../puzzle_input.txt", "r")
print(f"answer to puzzle input is: {solve(puzzle_input)}")
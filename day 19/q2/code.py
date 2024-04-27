# pass a range to functions and return all ranges that pass
# calculate number of combinations from all passing ranges

# answer: 131550418841958


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
        value = (
            value.replace("=", ":")
            .replace("{", '{"')
            .replace(":", '":')
            .replace(",", ',"')
        )
        values.append(eval(value))
    return values


def eval_function(func, value, functions):
    ranges_to_return = []

    for condition, body in func:
        if condition == True:
            if body == "A":
                ranges_to_return += [value]
            elif body != "R":
                ranges_to_return += eval_function(functions[body], value, functions)
            continue
        
        property = condition[0]
        comparator = condition[1]
        check = int(condition[2:])

        ## if we fail, set value, if we succeed make new value and recurse
        if comparator == ">":
            current_range = value[property]
            new_success_range = (check + 1, current_range[1])
            new_failed_range = (current_range[0], check)

            success_value = value.copy()
            success_value[property] = new_success_range
            if(new_success_range[1] >= new_success_range[0]):
                ranges_to_return += eval_function(functions[body], success_value, functions)

            value[property] = new_failed_range
        elif comparator == "<":
            current_range = value[property]
            new_success_range = (current_range[0], check - 1)
            new_failed_range = (check, current_range[1])

            success_value = value.copy()
            success_value[property] = new_success_range
            if(new_success_range[1] >= new_success_range[0]):
                ranges_to_return += eval_function(functions[body], success_value, functions)
            value[property] = new_failed_range

    return ranges_to_return

def get_all_accepted_ranges(functions, value):
    return eval_function(functions["in"], value, functions)


def solve(file):
    raw_functions, _ = get_raw_data(file)
    functions = get_functions_dict(raw_functions)  # name: [list of (condition, body)]
    functions["A"] = [(True, "A")]
    functions["R"] = [(True, "R")]
    accepted_values = get_all_accepted_ranges(
        functions, {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    )
    return sum([(v["x"][1] - v["x"][0] + 1) *
                (v["m"][1] - v["m"][0] + 1) *
                (v["a"][1] - v["a"][0] + 1) *
                (v["s"][1] - v["s"][0] + 1) for v in accepted_values])


sample_input = open("../sample_input.txt", "r")
assert_equals(solve(sample_input), 167409079868000)
puzzle_input = open("../puzzle_input.txt", "r")
print(f"answer to puzzle input is: {solve(puzzle_input)}")

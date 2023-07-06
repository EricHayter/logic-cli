import math
import itertools

def simplify_function(func: dict) -> dict:
    num_vars = log(len(func), 2)
    # check for paris of values/prime implicants
    # check from biggest to smallest
    # e.g. can it be simplified to True or False?
    # then can it be simplified down to one variable?
    true_inputs = []
    for c in input_combos(num_vars):
        if func[c]:
            true_inputs.append(c)


# create a generator to make combos e.g.
# (None, None, None, None) (True, None, None, None) ...
for i in itertools.product([None, True, False], repeat = 4):
    print(i)


def input_combos(n: int, values: list[list[bool]] = []) -> list[tuple]:
    if n <= 0:
        return [tuple(c) for c in values]
    else:
        if not values:
            values = [[]]
        values = [e + [v] for e in values for v in (False, True)]
        return input_combos(n - 1, values)

    

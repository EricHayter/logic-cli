import math
import itertools
import operator as op

def simplify_function(func: dict) -> dict:
    num_vars = math.log(len(func), 2)
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
def get_implicants(n: int) -> list:
    imp = list(set(itertools.product([True, False, None], repeat = n)))
    return sorted(imp, key = lambda l : l.count(None), reverse=True)

def input_combos(n: int, values: list[list[bool]] = [[]]) -> list[tuple]:
    if n <= 0:
        return [tuple(c) for c in values]
    else:
        values = [e + [v] for e in values for v in (False, True)]
        return input_combos(n - 1, values)

for i in get_implicants(3):
    print(i)
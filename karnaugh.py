import math
import itertools

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
    c = 0
    while c <= n:
        # this isn't efficient since the thing will mix Nones
        # this isn't working correctly atm
        for value in itertools.combinations([True, False], c):
            print(value)
            for i in set(itertools.permutations((n- c) * [None] + list(value), n)):
                yield i
        c += 1

def input_combos(n: int, values: list[list[bool]] = []) -> list[tuple]:
    if n <= 0:
        return [tuple(c) for c in values]
    else:
        if not values:
            values = [[]]
        values = [e + [v] for e in values for v in (False, True)]
        return input_combos(n - 1, values)

    
print(len([x for x in get_implicants(4)]))
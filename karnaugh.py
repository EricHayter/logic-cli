import math
import itertools

def simplify_function(func: dict) -> dict:
    num_vars = int(math.log(len(func), 2))
    # check for paris of values/prime implicants
    # check from biggest to smallest
    # e.g. can it be simplified to True or False?
    # then can it be simplified down to one variable?
    prime_implicants = []
    minterms = [c for c in func if func[c]]
    for implicant in get_implicants(num_vars):
        if not minterms:
            break
        included = included_minterms(func.keys(), implicant)
        for m in included:
            if not func[m]: # implicant can't wont work if minterm is false
                break
        else:
            prime_implicants.append(implicant)
            for i in included:
                if i in minterms:
                    minterms.remove(i)
    return prime_implicants


def included_minterms(minterms: list[tuple], implicant: tuple) -> list[tuple]:
    included = []
    for minterm in minterms:
        for m, i in zip(minterm, implicant):
            if i and i != m:
                break
            elif i == False and i != m:
                break
        else:
            included.append(minterm)
    return included


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


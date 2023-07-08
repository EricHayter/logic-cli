import math
import itertools


def simplify_function(func: dict, variables: list[str], SOP: bool = True) -> str:
    num_vars = int(math.log(len(func), 2))
    prime_implicants = []
    if SOP:
        minterms = [c for c in func if func[c]]
    else:
        [c for c in func if not func[c]]
    for implicant in get_implicants(num_vars):
        if not minterms:
            break
        included = included_minterms(func.keys(), implicant)
        for m in included:
            if not func[m]:  # implicant can't wont work if minterm is false
                break
        else:
            prime_implicants.append(implicant)
            for i in included:
                if i in minterms:
                    minterms.remove(i)

    if SOP:
        print(prime_implicants)
        for idx, term in enumerate(prime_implicants):
            if term == 0:
                prime_implicants[idx] = '~' + variables[idx]
            else:
                prime_implicants[idx] = variables[idx]

        return '+'.join(['.'.join(term) for term in prime_implicants])


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


def get_implicants(n: int) -> list:
    imp = list(set(itertools.product([True, False, None], repeat=n)))
    return sorted(imp, key=lambda l: l.count(None), reverse=True)


def input_combos(n: int, values: list[list[bool]] = [[]]) -> list[tuple]:
    if n <= 0:
        return [tuple(c) for c in values]
    else:
        values = [e + [v] for e in values for v in (False, True)]
        return input_combos(n - 1, values)

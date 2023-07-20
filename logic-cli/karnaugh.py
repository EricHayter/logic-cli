"""
karnaugh
"""

import itertools
from typing import List

from logic_function import LogicFunction
from hashable_dict import HashableDict


def compliment_function(func: LogicFunction) -> LogicFunction:
    """Finds the compliment of a function turning True to False and vise versa.
    Don't care values (None) will not be altered.

    :param func: A dictionary that takes in a tuple of boolean variable states
    and values of the output of the function
    :return: the compliment function
    """
    new_func = LogicFunction(func.copy(), func.variables)
    for key, value in new_func.items():
        if value is True:
            new_func[key] = False
        elif value is False:
            new_func[key] = True
    return new_func


def get_prime_implicants(func: LogicFunction) -> List[HashableDict]:
    """docstring"""
    prime_implicants = []
    minterms = [c for c in func if func[c] is True]
    for implicant in get_implicants(func.variables):
        if not minterms:  # stops the function when no minterms are left
            break
        included = included_minterms(func, implicant)
        for minterm in included:
            if func[minterm] is False:
                break
        else:
            prime = False
            for minterm in included:
                if minterm in minterms:
                    minterms.remove(minterm)
                    prime = True
            if prime:
                prime_implicants.append(implicant)
    return prime_implicants


def get_essential_implicants(
    func: LogicFunction,
    prime_implicants: List[HashableDict],
) -> List[HashableDict]:
    """docstring"""
    essential_implicants: List[HashableDict] = []
    for implicant in prime_implicants:
        other_implicants = [i for i in prime_implicants if i != implicant]
        if is_essential(func, other_implicants, implicant):
            essential_implicants.append(implicant)
    return essential_implicants


def is_essential(
    func: LogicFunction,
    implicants: list[HashableDict],
    implicant: HashableDict
) -> bool:
    """
    docstring
    """
    # get the list of minterms in the implicant we want
    # breakpoint()
    minterms = included_minterms(func, implicant)
    for imp in implicants:
        for minterm in included_minterms(func, imp):
            if minterm in minterms:
                minterms.remove(minterm)
    return bool(minterms)


def included_minterms(
    func: LogicFunction, implicant: HashableDict
) -> list[HashableDict]:
    """This function finds all of the minterms grouped in a implicant"""
    included = []
    terms = get_minterms(func.variables)
    for term in terms:
        for variable in implicant:
            if term[variable] != implicant[variable]:
                break
        else:
            included.append(term)
    return included


def get_minterms(variables: tuple[str, ...]):
    """Yields all of the minterms of a function"""
    num_variables = len(variables)
    truth_combos = itertools.product([True, False], repeat=num_variables)
    for truth_values in truth_combos:
        yield HashableDict(zip(variables, truth_values))


def get_implicants(variables: tuple[str, ...]):
    """Yields all implicants from a given set of variables"""
    num_variables = len(variables)
    for i in range(1, num_variables + 1):
        for used_variables in itertools.combinations(variables, i):
            truth_combos = itertools.product([True, False], repeat=i)
            for truth_values in truth_combos:
                yield HashableDict(zip(used_variables, truth_values))


def get_sop(prime_implicants: list[HashableDict]) -> str:
    """Gives a string representation of a set of prime implicants in sum of product format

    :param prime_implicants: a list of prime implicants
    :param variables: names of each variable for each index in the prime implicant tuples
    :return: a string representation of the sum of products
    """
    # create a check for contradictions and tautologies
    sop_str = []
    for implicant in prime_implicants:
        atoms = [convert_atom(s, v) for s, v in implicant.items()]
        implicant_str = f"({'.'.join(atoms)})"
        sop_str.append(implicant_str)
    return "+".join(sop_str)


def get_pos(
        prime_implicants: list[tuple[bool | None]], variables: tuple[str]) -> str:
    """docstring"""
    pos_str = []
    for implicant in prime_implicants:
        implicant = [
            convert_atom(
                i, z) for i, z in zip(
                implicant, variables)]
        implicant = [i for i in implicant if i is not None]
        implicant = f"({'+'.join(implicant)})"
        pos_str.append(implicant)
    return ".".join(pos_str)


def convert_atom(symbol: str, value: bool) -> str:
    """docstring"""
    if value is True:
        return symbol

    return "~" + symbol

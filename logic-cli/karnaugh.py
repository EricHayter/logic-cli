"""
karnaugh
"""

import itertools
from typing import List

from logic_function import LogicFunction
from function_input import FunctionInput


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


def get_prime_implicants(func: LogicFunction) -> List[FunctionInput]:
    """Returns the shortest possible list of prime implicants to represent a function.

    :param func: a dictionary with tuple-boolean pairs to represent the input and output of a logical function
    :return: a list of prime implicants used to simplify the function
    """
    assert isinstance(func, LogicFunction)
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
    prime_implicants: List[FunctionInput],
) -> List[FunctionInput]:
    """
    docstring
    """
    essential_implicants: List[FunctionInput] = []
    for implicant in prime_implicants:
        if is_essential(func, prime_implicants, implicant):
            essential_implicants.append(implicant)
    return essential_implicants


def is_essential(
    func: LogicFunction, implicants: list[FunctionInput], implicant: FunctionInput
) -> bool:
    """
    docstring
    """
    # get the list of minterms in the implicant we want
    minterms = included_minterms(func, implicant)
    for imp in implicants:
        for minterm in included_minterms(func, imp):
            if minterm in minterms:
                minterms.remove(minterm)
    return bool(minterms)


def included_minterms(
    func: LogicFunction, implicant: FunctionInput
) -> list[FunctionInput]:
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
        yield FunctionInput(zip(variables, truth_values))


def get_implicants(variables: tuple[str, ...]):
    """Yields all implicants from a given set of variables"""
    num_variables = len(variables)
    for i in range(1, num_variables + 1):
        for used_variables in itertools.combinations(variables, i):
            truth_combos = itertools.product([True, False], repeat=i)
            for truth_values in truth_combos:
                yield FunctionInput(zip(used_variables, truth_values))


def get_sop(prime_implicants: list[tuple[bool | None]], variables: tuple[str]) -> str:
    """Gives a string representation of a set of prime implicants in sum of product format

    :param prime_implicants: a list of prime implicants
    :param variables: names of each variable for each index in the prime implicant tuples
    :return: a string representation of the sum of products
    """
    sop_str = []
    if len(prime_implicants) == 1 and set(prime_implicants[0]) == {None}:
        return "T"
    elif not prime_implicants:
        return "F"
    for implicant in prime_implicants:
        implicant = [convert_atom(i, z) for i, z in zip(implicant, variables)]
        implicant = [i for i in implicant if i is not None]
        implicant = f"({'.'.join(implicant)})"
        sop_str.append(implicant)
    return "+".join(sop_str)


def get_pos(prime_implicants: list[tuple[bool | None]], variables: tuple[str]) -> str:
    """Gives a string representation of a set of prime implicants in product of sum format

    :param prime_implicants: a list of prime implicants
    :param variables: names of each variable for each index in the prime implicant tuples
    :return: a string representation of the product of sums
    """
    pos_str = []
    if len(prime_implicants) == 1 and set(prime_implicants[0]) == {None}:
        return "T"
    elif not prime_implicants:
        return "F"
    for implicant in prime_implicants:
        implicant = [convert_atom(i, z) for i, z in zip(implicant, variables)]
        implicant = [i for i in implicant if i is not None]
        implicant = f"({'+'.join(implicant)})"
        pos_str.append(implicant)
    return ".".join(pos_str)


def convert_atom(value: bool | None, symbol: str) -> str | None:
    """Returns the string representation of a symbol. If a symbol called 'A' is given with a value of False "~A" will
    be returned or "A" if value is True. If the value of the symbol is set to None will be returned.

    :param value: the boolean value of the symbol
    :param symbol: the name of the symbols e.g. A, B, C,...
    :return: A string representation of the symbol
    """
    if value is None:
        return None
    elif value is True:
        return symbol
    elif value is False:
        return "~" + symbol

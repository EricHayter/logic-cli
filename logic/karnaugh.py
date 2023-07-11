import math
import itertools


def compliment_function(func: dict[tuple[bool], bool | None]) -> dict[tuple[bool], bool | None]:
    """ Finds the compliment of a function turning True to False and vise versa. Don't care values (None) will not
    be altered.

    :param func: A dictionary that takes in a tuple of boolean variable states and values of the output of the function
    :return: the compliment function
    """
    f = func.copy()
    for key, value in f.items():
        if value is True:
            f[key] = False
        elif value is False:
            f[key] = True
    return f


def simplify_function(func: dict[tuple[bool], bool | None]) -> list[tuple[bool | None] | bool]:
    """ Returns the shortest possible list of prime implicants to represent a function.

    :param func: a dictionary with tuple-boolean pairs to represent the input and output of a logical function
    :return: a list of prime implicants used to simplify the function
    """
    num_vars = int(math.log(len(func), 2))
    prime_implicants = []
    minterms = [c for c in func if func[c] is True]
    for implicant in get_implicants(num_vars):
        if not minterms:  # stops the function when no minterms are left
            break
        included = included_minterms(list(func.keys()), implicant)
        for m in included:
            if func[m] is False:
                break
        else:
            prime = False  # checking if implicant is prime
            for i in included:
                if i in minterms:
                    minterms.remove(i)
                    prime = True
            if prime is True:
                prime_implicants.append(implicant)
    return prime_implicants


def included_minterms(minterms: list[tuple[bool | None]], implicant: tuple[bool | None]) -> list[tuple[bool | None]]:
    """ Returns a filtered list of minterms such that each value inside each of the minterms is equal to implicant.
    However, if the value of a variable in the implicant is None the minterm will match no matter what.

    :param minterms: a list of tuples containing boolean values to represent logical minterms
    :param implicant: a single implicant containing boolean and/or none values to represent implicants
    :return: a filtered list of minterms that are contained within the implicant
    """
    included = []
    for minterm in minterms:
        for m, i in zip(minterm, implicant):
            if i is True and m is False:
                break
            elif i is False and m is True:
                break
        else:
            included.append(minterm)
    return included


def get_implicants(n: int) -> list[tuple[bool | None]]:
    """ Gives a list of all possible combinations of T, F, and None such that combinations with more Nones are at
    the beginning of the list.

    :param n: The number of variables included in each tuple
    :return: a list containing all possible combinations of T, F
    """
    imp = list(set(itertools.product([True, False, None], repeat=n)))
    return sorted(imp, key=lambda l: l.count(None), reverse=True)


def print_sop(prime_implicants: list[tuple[bool | None]],  variables: tuple[str]) -> str:
    sop_str = []
    for implicant in prime_implicants:
        implicant = [convert_atom(i, z) for i, z in zip(implicant, variables)]
        implicant = [i for i in implicant if i is not None]
        implicant = f"({'.'.join(implicant)})"
        sop_str.append(implicant)
    return '+'.join(sop_str)


def print_pos(prime_implicants: list[tuple[bool | None]],  variables: tuple[str]) -> str:
    pos_str = []
    for implicant in prime_implicants:
        implicant = [convert_atom(i, z) for i, z in zip(implicant, variables)]
        implicant = [i for i in implicant if i is not None]
        implicant = f"({'+'.join(implicant)})"
        pos_str.append(implicant)
    return '.'.join(pos_str)


def convert_atom(value: bool | None, symbol: str) -> str | None:
    """ Returns the string representation of a symbol. If a symbol called 'A' is given with a value of False "~A" will
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
        return '~' + symbol

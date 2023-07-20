"""
docstring
"""

import itertools

from function_input import FunctionInput


def find_parenthesis(characters: list[object]) -> tuple[int, int]:
    """
    finds the outermost set of parenthesis in a function.
    returns a tuple (s,f) where s is the index of the opening parenthesis
    in the list and f is the index of the closing parenthesis in the list
    """
    paren_open = False
    count = 0
    for idx, char in enumerate(characters):
        if char == "(":
            paren_open = True
            count += 1
        elif char == ")":
            count -= 1
        if count == 0 and paren_open:
            return characters.index("("), idx
    raise ValueError("No closing bracket in the list of characters")


def input_combos(symbols: tuple[str, ...]):
    """
    return all possible inputs for a function given a tuple of all function
    variable names
    """
    num_vars = len(symbols)
    truth_values = itertools.product([True, False], repeat=num_vars)
    for truth_combo in truth_values:
        combo = FunctionInput()
        for variable, value in zip(symbols, truth_combo):
            combo[variable] = value
        yield combo


def replace_range(elements: list, start: int, stop: int, replace: object) -> list:
    """
    docstring
    """
    new_elements = elements[:]
    for _ in range(stop - start):
        new_elements.pop(start)
    new_elements[start] = replace
    return new_elements

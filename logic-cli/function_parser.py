""" Function Parser
simple module for parsing a string into a logical function
the function is read into a FunctionParser object after being passed in as a
string and then can be evaluted given a set of boolean values in a tuple
or a truth table for the function can be given in the format of a dictionary
"""


from typing import List
from ast import literal_eval

from karnaugh import included_minterms
from util_functions import find_parenthesis, replace_range, input_combos
from logic_function import LogicFunction
from hashable_dict import HashableDict


def parse_function(file_name: str) -> LogicFunction:  # should take io.
    """
    fill this docstring
    """
    with open(file_name, encoding='utf-8') as file:
        proposition = file.readline()
        symbols = get_symbols(proposition)
        truth_table = get_truth_table(list(proposition), symbols)
        logic_function = LogicFunction(truth_table, symbols)
        for line in file:
            terms = literal_eval(line.strip())
            for minterm in included_minterms(logic_function, terms):
                logic_function[minterm] = None

    return logic_function


def get_symbols(proposition: str) -> tuple[str, ...]:
    # make this return a tuple of the symbols instead?
    """
    Assigns each of the uppercase letters a location in the symbols
    instance dictionary for symbols to be reused for reoccuring symbols
    """
    symbols: List[str] = []
    for symbol in proposition:
        if "A" <= symbol <= "Z":
            if symbol not in symbols:
                symbols.append(symbol)
        elif symbol not in [
            "~",
            "(",
            ")",
            ".",
            "+",
        ]:
            idx = proposition.index(symbol)
            raise ValueError(f"Invalid symbol at position {idx}")
    return tuple(symbols)


def update_output(func: LogicFunction, func_input: HashableDict,
                  new_output: bool | None) -> None:
    """docstring"""
    func[func_input] = new_output


def evaluate(expression: list, symbols: HashableDict) -> bool:
    """
    fill this docstring
    """
    expression = expression[:]
    while "(" in expression:
        start, stop = find_parenthesis(expression)
        enclosed_logic = evaluate(expression[start + 1: stop], symbols)
        expression = replace_range(expression, start, stop, enclosed_logic)
    for idx, char in enumerate(expression):
        if isinstance(char, str) and "A" <= char <= "Z":
            expression[idx] = symbols[char]
    while "~" in expression:
        loc = expression.index("~")
        if loc == len(expression):
            raise ValueError("Negation symbol is negating nothing")
        expression = replace_range(
            expression, loc, loc + 1, not expression[loc + 1])
    while "+" in expression:
        loc = expression.index("+")
        if loc == 0 or loc == len(expression):
            raise ValueError(
                "OR statements must take two expressions to evaluate")
        expression = replace_range(
            expression, loc - 1, loc +
            1, expression[loc - 1] or expression[loc + 1]
        )
    while "." in expression:
        loc = expression.index(".")
        if loc == 0 or loc == len(expression):
            raise ValueError(
                "Incorrect formatting, AND statements must take two expressions to evaluate"
            )
        expression = replace_range(
            expression,
            loc - 1,
            loc + 1,
            expression[loc - 1] and expression[loc + 1],
        )
    return expression[0]

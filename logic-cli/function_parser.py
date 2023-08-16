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
    Given a file name containing a logical expression parse the function to give a logic function object that contains
    all possible inputs and respective outputs of the given expression.
    """
    with open(file_name, encoding='utf-8') as file:
        proposition = file.readline()
        symbols = get_symbols(proposition)
        truth_table = get_truth_table(list(proposition), symbols)
        logic_function = LogicFunction(truth_table, symbols)
        for line in file:
            mapping = literal_eval(line.strip())
            for minterm in included_minterms(logic_function, mapping):
                logic_function[minterm] = None

    return logic_function


def get_symbols(expression: str) -> tuple[str, ...]:
    """
    Creates a tuple consisting of all uppercase variables used in an expression
    """
    symbols: List[str] = []
    for symbol in expression:
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
            idx = expression.index(symbol)
            raise ValueError(f"Invalid symbol at position {idx}")
    return tuple(symbols)


def get_truth_table(expression: list, symbols: tuple[str, ...]) -> dict:
    """
    Creates a truth table in the format of a dictionary for all possible inputs of the function. keys of the dictionary
    represent the boolean mappings to each of the variables in the expression and values of the dictionary represent
    the output of the function (True, False, None (Don't care values))
    """
    truth_table = dict()
    for mapping in input_combos(symbols):
        truth_table[mapping] = evaluate(expression, mapping)
    return truth_table


def evaluate(expression: list, mapping: HashableDict) -> bool:
    """
    Outputs the value of a given expression with a set of variable boolean mappings (inputs) to the logical function.
    """
    expression = expression[:]
    while "(" in expression:
        start, stop = find_parenthesis(expression)
        enclosed_logic = evaluate(expression[start + 1: stop], mapping)
        expression = replace_range(expression, start, stop, enclosed_logic)
    for idx, char in enumerate(expression):
        if isinstance(char, str) and "A" <= char <= "Z":
            expression[idx] = mapping[char]
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
            expression, loc - 1, loc + 1, expression[loc - 1] or expression[loc + 1]
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

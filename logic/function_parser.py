""" Function Parser
simple module for parsing a string into a logical function
the function is read into a FunctionParser object after being passed in as a 
string and then can be evaluted given a set of boolean values in a tuple
or a truth table for the function can be given in the format of a dictionary

TODO:
    make this functional
"""

from typing import Dict
from logic.utils import input_combos, find_parenthesis, replace_range
from logic.function import LogicFunction

def parse_function(proposition: str) -> LogicFunction:
    """
    fill this docstring
    """
    symbols = init_symbols(proposition)
    symbols['f'] = True
    return LogicFunction({}, ('A', ('B')))

def init_symbols(proposition: str) -> dict:
    """
        Assigns each of the uppercase letters a location in the symbols 
        instance dictionary for symbols to be reused for reoccuring symbols
        """
    symbols: Dict[str, bool | None ] = {}
    for symbol in proposition:
        if "A" <= symbol <= "Z":
            if symbol not in symbols:
                symbols[symbol] = True
        elif symbol not in [
                    "~",
                    "(",
                    ")",
                    ".",
                    "+",
                    ]:
            idx = proposition.index(symbol)
            raise ValueError(f"Invalid symbol at position {idx}")
    return symbols

def evaluate(expression: str, symbols: dict) -> bool:
    """
    fill this docstring
    """
    expression = expression[:]
    while "(" in expression:
        start, stop = find_parenthesis(expression)
        enclosed_logic = self.evaluate(expression[start + 1: stop], values)
        expression = replace_range(expression, start, stop, enclosed_logic)
    for idx, ch in enumerate(expression):
        if type(ch) == str and "A" <= ch <= "Z":
            expression[idx] = self.symbols[ch]
    while "~" in expression:
        loc = expression.index("~")
        if loc == len(expression):
            raise Exception("Negation symbol is negating nothing")
        expression = replace_range(
                expression, loc, loc + 1, not expression[loc + 1])
    while "+" in expression:
        loc = expression.index("+")
        if loc == 0 or loc == len(expression):
            raise Exception(
                    "OR statements must take two expressions to evaluate")
        expression = replace_range(
                expression, loc - 1, loc +
                1, expression[loc - 1] or expression[loc + 1]
                )
    while "." in expression:
        loc = expression.index(".")
        if loc == 0 or loc == len(expression):
            raise Exception(
                    "Incorrect formatting, AND statements must take two expressions to evaluate")
        expression = replace_range(
                expression,
                loc - 1,
                loc + 1,
                expression[loc - 1] and expression[loc + 1],
                )
    return expression[0]

def get_variables(self) -> tuple:
    return tuple(self.symbols.keys())

def get_truth_table(self) -> dict:
    combinations = input_combos(len(self.symbols))
    truth_table = dict()
    for c in combinations:
        truth_table[c] = self.evaluate(self.proposition, c)
    return truth_table

import re
from karnaugh import input_combos

# not is not working nicely for me
# either need a smart fix for the not isseue in the code
# or make another function that solves the problems that I am having

class FunctionParser:
    def __init__(self, proposition: str) -> None:
        self.symbols = dict()
        self.init_symbols(proposition)
        self.logic_function = self.parse_logic(list(proposition))

    def init_symbols(self, proposition: str) -> None:
        matches = re.findall(r"[~().+A-Z]", proposition)
        if not matches:
            print("not matching anything")
            return

        for symbol in matches:
            if symbol >= "A" and symbol <= "Z":
                if symbol not in self.symbols:
                    self.symbols[symbol] = True
            elif symbol not in [
                "~",
                "(",
                ")",
                ".",
                "+",
            ]:
                raise Exception("Symbol must be in range [A-Z]")

    def parse_logic(self, expression: list[object]) -> list:
        if "(" in expression:
            start, stop = find_parenth_pair(expression)
            logic = self.parse_logic(expression[start + 1 : stop])
            expression = replace_range(expression, start, stop, logic)
        for idx, ch in enumerate(expression):
            if type(ch) is str and ch >= "A" and ch <= "Z":
                expression[idx] = self.sym(ch)
        while "~" in expression:
            loc = expression.index("~")
            if loc == len(expression):
                raise Exception("Negation symbol is negating nothing")
            breakpoint()
            function = expression[loc + 1]
            expression = replace_range(expression, loc, loc + 1, lambda : not function())
        while "+" in expression:
            loc = expression.index("+")
            if loc == 0 or loc == len(expression):
                raise Exception(
                    "Incorrect formatting, OR statements must take two expressions to evaluate"
                )
            expression = replace_range(
                expression, loc - 1, loc + 1, expression[loc - 1] or expression[loc + 1]
            )
        while "." in expression:
            loc = expression.index(".")
            if loc == 0 or loc == len(expression):
                raise Exception(
                    "Incorrect formatting, AND statements must take two expressions to evaluate"
                )
            replace_range(
                expression,
                loc - 1,
                loc + 1,
                expression[loc - 1] and expression[loc + 1],
            )
        return expression[0]

    def evaluate(self, values: list = None, mappings: dict = None) -> bool:
        if mappings is not None:
            for key, value in mappings.items():
                if key not in self.symbols:
                    raise Exception(f"Uknown symbol {key}")
                if type(value) is not bool:
                    raise Exception(f"Value of {key} must be a boolean type")
                self.symbols[key] = value
        elif values is not None:
            if len(values) != len(self.symbols):
                raise Exception("Inavlid amount of variables")
            for key, value in zip(self.symbols, values):
                if type(value) is bool:
                    self.symbols[key] = value
                else:
                    raise Exception("value must be of type bool")
        else:
            raise Exception("must provide either values list or mappings")
        return self.logic_function()

    def get_truth_table(self) -> dict:
        combinations = input_combos(len(self.symbols))
        truth_table = dict()
        for c in combinations:
            truth_table[c] = self.evaluate(c)
        return truth_table

    def get_symbols(self) -> list[str]:
        return list(self.symbols.keys())

    def sym(self, symbol: str):
        """
        returns a wrapper function to retrieve the value of the given symbol\
        WORKS PERFECTLY SMARTEST PROGRAMMER THAT EVER LIVED TYPE BEAT
        """
        if symbol not in self.symbols:
            raise Exception(f"Unkown symbol {symbol}")
        return lambda: self.symbols[symbol]


def find_parenth_pair(characters: list[object]) -> int:
    # maybe remake this into find pair type beat
    # then return tuple for start + stop
    paren_open = False
    count = 0
    for idx, chr in enumerate(characters):
        if chr == "(":
            paren_open = True
            count += 1
        elif chr == ")":
            count -= 1
        if count == 0 and paren_open:
            return characters.index("("), idx
    raise Exception("No closing bracket in the list of characters")


def replace_range(l: list, start: int, stop: int, replace: object) -> list:
    for _ in range(stop - start):
        l.pop(start)
    l[start] = replace
    return l

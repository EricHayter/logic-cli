from logic.utils import input_combos, find_parenthesis, replace_range


class FunctionParser:
    def __init__(self, proposition: str) -> None:
        self.proposition = list(proposition)
        self.symbols = dict()
        self.init_symbols()

    def init_symbols(self) -> None:

        for symbol in self.proposition:
            if "A" <= symbol <= "Z":
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

    def evaluate(self, expression: list, values: list) -> bool:
        expression = expression[:]
        for key, value in zip(self.symbols, values):
            self.symbols[key] = value
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

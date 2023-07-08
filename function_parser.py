from karnaugh import input_combos


class FunctionParser:
    def __init__(self, proposition: str) -> None:
        self.proposition = list(proposition)
        self.symbols = dict()
        self.init_symbols()

    def init_symbols(self) -> None:
        for symbol in self.proposition:
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

    def evaluate(self, values: list) -> bool:
        expression = self.proposition[:]
        for key, value in zip(self.symbols, values):
            self.symbols[key] = value
        if "(" in expression:
            start, stop = find_parenth_pair(expression)
            logic = self.parse_logic(expression[start + 1: stop])
            expression = replace_range(expression, start, stop, logic)
        for idx, ch in enumerate(expression):
            if type(ch) is str and ch >= "A" and ch <= "Z":
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

    def get_truth_table(self) -> dict:
        combinations = input_combos(len(self.symbols))
        truth_table = dict()
        for c in combinations:
            truth_table[c] = self.evaluate(c)
        return truth_table

    def get_symbols(self) -> list[str]:
        return list(self.symbols.keys())


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
    c = l[:]
    for _ in range(stop - start):
        c.pop(start)
    c[start] = replace
    return c

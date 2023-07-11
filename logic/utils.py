def input_combos(n: int, values: list[list[bool]] = [[]]) -> list[tuple]:
    if n <= 0:
        return [tuple(c) for c in values]
    else:
        values = [e + [v] for e in values for v in (False, True)]
        return input_combos(n - 1, values)


def find_parenthesis(characters: list[object]) -> int:
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
    raise Exception("No closing bracket in the list of characters")


def replace_range(l: list, start: int, stop: int, replace: object) -> list:
    c = l[:]
    for _ in range(stop - start):
        c.pop(start)
    c[start] = replace
    return c

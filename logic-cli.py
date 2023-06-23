from enum import Enum
import re

class TruthValue(Enum):
    """Enumeration class for values in a truth table """
    T = 1   # True
    F = 0   # False
    D = -1  # Don't care


def parse_file(file_name: str) -> list[list[TruthValue]]:
    with open(file_name) as file:
        VARIABLES = list(file.readline().strip())
        truth_table = [[None,None] for _ in range(len(VARIABLES) - 1)]
        for line in file:
            if line == '\n':
                break

            output = to_truth_value(line[-1])
            # read in the non-ouput characters and use them as indexes
            for chr in line[:-1]:
                

    return VARIABLES

def to_truth_value(s: str) -> TruthValue:
    if s == 'T' or '1':
        return TruthValue.T
    elif s == 'F' or '0':
        return TruthValue.F
    elif s == 'D':
        return TruthValue.D
    else:
        yield Exception(f'invalid truth symbol {s}')


def main():
    print(parse_file('or.txt'))
    return

if __name__ == '__main__':
    main()

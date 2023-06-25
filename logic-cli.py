from enum import Enum
import re

class TruthValue(Enum):
    """Enumeration class for values in a truth table """
    T = True   # True
    F = False   # False
    D = None  # Don't care

    def __repr__(self):
        return self.name


def parse_file(file_name: str) -> list[list[TruthValue]]:
    truth_table = dict()
    # read in the function
    # parse it into an actual python function to calculate the output

    if False:
        with open(file_name) as file:
            truth_table['VARIABLES'] = list(file.readline().strip())
            for line in file:
                line = line.strip()
                if line == '\n':
                    break
               
                # still not error catching in it
                output = to_truth_value(line[-1])
                truth_values = tuple([to_truth_value(s) for s in line[:-1]])
                truth_table[truth_values] = output
                
    return truth_table

def input_combos(n: int, values:list[list[TruthValue]] = []) -> list[tuple(TruthValue)]:
    if n <= 0:
        return [tuple(c) for c in values]
    else:
        if not values:
            values = [[]]
        values = [e + [v] for e in values for v in (TruthValue.F, TruthValue.T)]
        return input_combos(n - 1, values)


def to_truth_value(s: str) -> TruthValue:
    if s == 'T' or s == '1':
        return TruthValue.T
    elif s == 'F' or s == '0':
        return TruthValue.F
    elif s == 'D':
        return TruthValue.D
    else:
        raise Exception(f'invalid truth symbol {s}')


def main():
    #print(parse_file('or.txt'))
    print(input_combos(3))
    return

if __name__ == '__main__':
    main()

"""table parser functions"""
import csv

from hashable_dict import HashableDict
from logic_function import LogicFunction


def parse_table(csv_file: str) -> LogicFunction:
    """docstring"""
    with open(csv_file, encoding='utf-8') as file:
        reader = csv.reader(file)
        variables = tuple(next(reader))[:-1]
        truth_table = {}
        for row in reader:
            row = [element.strip() for element in row]
            key = HashableDict(zip(variables, map(str_to_bool, row[:-1])))
            truth_table[key] = str_to_bool(row[-1])
    return LogicFunction(truth_table, variables)


def str_to_bool(value: str) -> bool | None:
    """docstring"""
    if value in ('T', '1', 'True'):
        return True
    if value in ('F', '0', 'False'):
        return False
    if value == 'D':
        return None
    raise ValueError("Value of str must be either T or F")

"""docstring"""
import csv
from io import TextIOWrapper

from hashable_function import HashableDict
from logic_function import LogicFunction


def parse_table(csv_file: str) -> LogicFunction:
    """docstring"""
    with open(csv_file) as file:
        reader = csv.DictReader(file)
    if reader.fieldnames is None:
        raise ValueError("Must provide file with CSV format with headers")
    if 'OUT' not in reader.fieldnames:
        raise ValueError("must contain an out column in the function CSV")
    variables = tuple(
        fieldname for fieldname in reader.fieldnames if fieldname != 'OUT'
    )

    def parse_row(row: dict) -> HashableDict:
        row_dict = HashableDict()
        for variable in variables:
            row_dict[variable] = str_to_bool(row[variable])
        return row_dict

    truth_table = {}
    for row in reader:
        truth_table[parse_row(row)] = row['OUTPUT']
    return LogicFunction(truth_table, variables)


def str_to_bool(value: str) -> bool:
    """docstring"""
    if value == 'T':
        return True
    if value == 'F':
        return False
    raise ValueError("Value of str must be either T or F")

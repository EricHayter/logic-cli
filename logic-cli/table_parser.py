import csv


def parse_table(file_location: str) -> dict:
    try:
        with open(file_location, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = dict()
            for row in reader:
                row = [str_to_bool(elem) for elem in row]
                variables, output = tuple(row[:-1]), row[-1]
                rows[variables] = output
            return rows
    except IOError:
        raise Exception("Error: Unable to open the file.")


def str_to_bool(v: str) -> bool | None:
    if v == 'T':
        return True
    elif v == 'F':
        return False
    else:
        return None

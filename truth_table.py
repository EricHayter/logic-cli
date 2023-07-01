class TruthTable():
    def __init__(self, rows: list[list]) -> None:
        self.truth_table = dict()

        # should be something along the lines of [[(variables), output],...]

        # all rows need to have the same amount of variables
        # needs to correct amount of rows
        if not (len(rows) > 0 and len(rows) == 2**len(rows[0])):
            raise Exception(
                'The number of rows should be equal to 2 to the number of variables in the function.')
        for row in rows:
            if len(row) != len(rows[0]):
                raise Exception(
                    'Rows must have consistent number of variables')
        # should I make a row class?
        

    def update_row(self, row: tuple[bool], value: bool) -> None:
        if value not in (True, False, None):
            raise Exception('value must of type bool or None')
        if row not in self.truth_table:
            raise Exception(f'the row {row} was not found in the truth table.')
        self.truth_table[row] = value

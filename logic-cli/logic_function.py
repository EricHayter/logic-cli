"""
simple data class for representing a function
"""

from hashable_dict import HashableDict


class LogicFunction(dict):
    def __init__(self, value, variables: tuple) -> None:
        self.__variables = variables
        for key in value:
            if not isinstance(key, HashableDict):
                raise TypeError("Keys must be HashableDicts")
            if len(key) != len(variables):
                raise ValueError("Keys must be of length variables")
            for variable in variables:
                if variable not in key:
                    raise ValueError("Keys must have the same variables as the function")
        dict.__init__(self, value)

    @property
    def variables(self) -> tuple:
        """
        Get the variables of a function
        """
        return self.__variables


def print_truth_table(func: LogicFunction) -> None:
    """
    """
    variables = func.variables
    print(*variables, 'output', sep='\t')
    for key, value in func.items():
        # print the boolean values of key and the output
        for i in key.values():
            print(i, end='\t')
        print(value)


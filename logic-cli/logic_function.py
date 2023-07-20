"""
simple data class for representing a function
"""


class LogicFunction(dict):
    def __init__(self, value, variables: tuple) -> None:
        dict.__init__(self, value)
        self.__variables = variables

    @property
    def variables(self) -> tuple:
        """
        Get the variables of a function
        """
        return self.__variables

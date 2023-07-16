"""
simple data class for representing a function
"""

class LogicFunction:
    def __init__(self, truth_table: dict, variables: tuple) -> None:
        self.variables = variables
        self.truth_table = truth_table
    def get_variables(self) -> tuple:
        """
        Get the variables of a function
        """
        return self.variables
    def get_truth_table(self) -> dict:
        """
        Returns a dictionary of key value pairs where the key values are
        possible inputs to the function and the value is the output of the 
        function
        """
        return self.truth_table

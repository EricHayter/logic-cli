"""
Module for implementing function input which is a immutable dictionary class
since the default dict implementation is not hashable
"""


class FunctionInput(dict):
    """
    simple immutable dict class for creating hashable mappings for variables
    """

    def __key(self):
        return tuple((k, self[k]) for k in sorted(self))

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()

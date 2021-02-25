# -*- coding: utf-8 -*-
from enum import Enum
from functools import reduce

class CodePegColor(Enum):
    """
    Possible colors for the secret code.
    """
    red = "R"
    magenta = "M"
    yellow = "Y"
    green = "G"
    pink = "P"
    cyan = "C"

    @classmethod
    def getAll(cls):
        """
        Returns a list of all available colors.
        """
        return [color for color in cls]

    @classmethod
    def getAllString(cls):
        """
        Returns a string of all available colors.
        """
        return reduce(lambda x, y: x + y.value, cls.getAll(), "")

    def __repr__(self):
        return str(self.name + "(" + self.value + ")")

class KeyPegColor(Enum):
    """
    Key code colors. Used when giving feedback on guesses.
    """
    white = "W"
    black = "B"
    none = "N"

    def __repr__(self):
        return str(self.name + "(" + self.value + ")")

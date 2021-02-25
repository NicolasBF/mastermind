# -*- coding: utf-8 -*-
from Pegs import CodePegColor, KeyPegColor
from random import sample

class CodeMaker(object):
    def __init__(self, code_length):
        self.code_length = code_length
        self.secret_code = CodeMaker.generateCode(code_length)

    def composeKeyCode(self, number_of_blacks, number_of_whites):
        """
        Compose a key code for giving feedback:
        One black means that a peg was in the correct position and color.
        One white means that a peg was of the correct color, in any position.
        One None means that the peg was neither.
        """
        number_of_nones = self.code_length - number_of_blacks - number_of_whites

        return [KeyPegColor.black for i in range(number_of_blacks)] \
             + [KeyPegColor.white for i in range(number_of_whites)] \
             + [KeyPegColor.none for i in range(number_of_nones)]

    def breakCode(self, color_list):
        """
        Try to guess the code.
        Return a list of key pegs based on the color_list guess.
        """
        reduced = self.secret_code[:]
        blacks = 0
        whites = 0
        for i, guess in enumerate(color_list):
            # Award black if the color and place is correct
            if guess == reduced[i]:
                reduced[i] = None
                blacks += 1

            else:
                # Award white if the color is somewhere in the secret_code,
                # but wouldn't be awarded a black.
                for j, secret in enumerate(reduced):
                    if guess == secret and color_list[j] != secret:
                        reduced[j] = None
                        whites += 1

        return self.composeKeyCode(blacks, whites)

    def evaluate(self, key_code):
        """
        Evaluate if key_code represents a win.
        """
        return sum(1 for x in key_code if x == KeyPegColor.black) == self.code_length

    def getSecretCode(self):
        return self.secret_code

    @staticmethod
    def generateCode(length):
        """
        Returns a randomized sample of all available colors.
        """
        return sample(CodePegColor.getAll(), length)

# -*- coding: utf-8 -*-
import re

from Pegs import CodePegColor
from CodeMaker import CodeMaker

class Game(object):
    def __init__(self, number_of_games, number_of_guesses, code_length):
        self.code_length = code_length
        self.number_of_games = number_of_games
        self.number_of_guesses = number_of_guesses
        self.codeMaker = None

        self.wins = 0
        self.losses = 0

    def loop(self):
        """
        Game loop. All user input is handleded here.
        """
        self.printHelp()

        number_of_guesses = self.number_of_guesses

        while self.number_of_games > 0:
            self.codeMaker = CodeMaker(self.code_length)
            print("A new game has started! A new secret code has been generated.")

            while self.number_of_guesses > 0:
                user_input = self.promptInput()

                # Parse commands
                if user_input in ["help", "h"]:
                    print("Available commands:")
                    print("  help, h".ljust(15), "Get help.")
                    print("  reveal, r".ljust(15), "Reveal the secret code (and exit - because where is the fun now).")
                    print("  quit, q".ljust(15), "Quit the game.")
                    continue

                elif user_input in ["quit", "q"]:
                    print("Exiting game.")
                    return

                elif user_input in ["revewal", "r"]:
                    print("Revealing the secret code.")
                    print("The code was:", self.codeMaker.getSecretCode())
                    break

                # Parse a guess
                parsed_input = self.parseUserString(user_input)
                if len(parsed_input) == 0:
                    print("Invalid input!")
                    continue

                self.number_of_guesses -= 1
                feedback = self.codeMaker.breakCode(parsed_input)

                if self.codeMaker.evaluate(feedback):
                    print("You guessed the code.")
                    self.wins += 1
                    break
                else:
                    print("The code maker provides key peg feedback.")
                    print("Guess:".ljust(13), parsed_input)
                    print("Feedback:".ljust(13), feedback)

                if self.number_of_guesses == 0:
                    print("Out of guesses!")
                    self.losses += 1
                else:
                    print("Guesses left:".ljust(13), self.number_of_guesses)

            self.number_of_guesses = number_of_guesses
            self.number_of_games -= 1

            print("Games left:".ljust(13), self.number_of_games)

        print("Out of games!")
        print("Total wins:", self.wins)
        print("Total losses:", self.losses)

    def promptInput(self):
        return input("> ")

    def parseUserString(self, user_string):
        """
        Parse user input string. Returns a list of first valid consecutive characters os size 'length'.
        If other characters are inserted, they will be discarded.
        """
        match = re.search((r"([{}])".format(CodePegColor.getAllString())) * self.code_length, user_string)

        if match != None:
            return [CodePegColor(x) for x in match.groups()]
        else:
            return []

    def printHelp(self):
        help_text = \
            """
    Welcome to Mastermind.

    Code length: {}
    Number of guesses: {}
    Number of games: {}

    Available colors are: {}
    Input example: > RRGC
            """.format(self.code_length,
                       self.number_of_guesses,
                       self.number_of_games,
                       CodePegColor.getAll())
        print(help_text)


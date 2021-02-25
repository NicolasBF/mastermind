# -*- coding: utf-8 -*-
import sys
assert sys.version_info >= (3,4)

from Game import Game
from CodeMaker import CodeMaker

import argparse

def main(args):
    game = Game(args.number_of_games, args.number_of_guesses, args.code_length)
    game.loop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--code-length", "-l", type=int, default=4,
                        help="Specify length of the code.")
    parser.add_argument("--number-of-games", "-g", type=int, default=1,
                        help="Specify number of rounds to play.")
    parser.add_argument("--number-of-guesses", "-n", type=int, default=10,
                        help="Specify the number of guesses per game round.")
    args = parser.parse_args()

    try:
        main(args)

    except KeyboardInterrupt:
        pass


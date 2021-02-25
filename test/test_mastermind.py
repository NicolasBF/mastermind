# -*- coding: utf-8 -*-
import Pegs
import Game
import CodeMaker

from random import seed

def join(l):
    return "".join([x.value for x in l])

def split(s):
    return [Pegs.CodePegColor(x) for x in list(s)]

class TestPegs(object):
    def test_getAllCodeColors(self):
        assert sorted(Pegs.CodePegColor.getAllString()) == sorted("RMYGPC")

class TestGame(object):
    def test_parseUserString(self):
        game = Game.Game(1, 10, 4)
        assert join(game.parseUserString("RRRR")) == "RRRR"
        assert join(game.parseUserString("RRRRR")) == "RRRR"
        assert join(game.parseUserString("RRR")) == ""
        assert join(game.parseUserString("")) == ""

        assert join(game.parseUserString("RMYG")) == "RMYG"
        assert join(game.parseUserString("RMYGRRRRR")) == "RMYG"
        assert join(game.parseUserString("BBBBBBBBRMYGRRRRRBBBB")) == "RMYG"

    def test_parseUserStringNone(self):
        game = Game.Game(1, 10, 0)
        assert join(game.parseUserString("")) == ""

    def test_parseUserStringSingle(self):
        game = Game.Game(1, 10, 1)
        assert join(game.parseUserString("R")) == "R"

class TestCodeMaker(object):
    def test_breakCode(self):
        maker = CodeMaker.CodeMaker(4)

        # Hack
        maker.secret_code = split("RYYY")

        assert join(maker.breakCode(split("RRRR"))) == "BNNN"
        assert join(maker.breakCode(split("CCRR"))) == "WNNN"
        assert join(maker.breakCode(split("GGGG"))) == "NNNN"
        assert join(maker.breakCode(split("GGGP"))) == "NNNN"
        assert join(maker.breakCode(split("RRYY"))) == "BBBN"
        assert join(maker.breakCode(split("YYYR"))) == "BBWW"
        assert join(maker.breakCode(split("RYYY"))) == "BBBB"

    def test_breakCode2(self):
        maker = CodeMaker.CodeMaker(4)

        # Hack
        maker.secret_code = split("RRYY")

        assert join(maker.breakCode(split("RRRY"))) == "BBBN"

    def test_breakCode3(self):
        maker = CodeMaker.CodeMaker(4)

        # Hack
        maker.secret_code = split("RMGP")

        assert join(maker.breakCode(split("PGMR"))) == "WWWW"
        assert join(maker.breakCode(split("PGRM"))) == "WWWW"
        assert join(maker.breakCode(split("GPMR"))) == "WWWW"
        assert join(maker.breakCode(split("PMGR"))) == "BBWW"

    def test_breakCode4(self):
        maker = CodeMaker.CodeMaker(3)

        # Hack
        maker.secret_code = split("GGG")

        assert join(maker.breakCode(split("PGM"))) == "BNN"

    def test_breakCode5(self):
        maker = CodeMaker.CodeMaker(1)

        # Hack
        maker.secret_code = split("G")

        assert join(maker.breakCode(split("G"))) == "B"
        assert join(maker.breakCode(split("P"))) == "N"

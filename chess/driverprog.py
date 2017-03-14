#driverprog.py   newgame.FEN    printboard.pyc       readchessfiles.py  readFENfunc.pyc   startpos.FEN        test.py
#fischspask.pgn  printboard.py  readchessfileFEN.py  readFENfunc.py     softeng1chess.py  testfuncpackage.py
#e2e4e7e5.FEN  newgame.FEN  rooktester.FEN  rooktest.FEN

import sys
import printboard
import readFENfunc
import legalmoves
import print_pretty
a = readFENfunc.readFEN('justkings.FEN')
printboard.printboard(a)
print('printed board now \n')
c = legalmoves.legal_list(a, 1)
print c
print('printing above move list in proper-ish chess notation')
print(print_pretty.purtyprint(c))

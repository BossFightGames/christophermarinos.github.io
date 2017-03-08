#driverprog.py   newgame.FEN    printboard.pyc       readchessfiles.py  readFENfunc.pyc   startpos.FEN        test.py
#fischspask.pgn  printboard.py  readchessfileFEN.py  readFENfunc.py     softeng1chess.py  testfuncpackage.py
import printboard
import readFENfunc
import legalmoves

a = readFENfunc.readFEN('rooktester.FEN')
printboard.printboard(a)
print('printed board now \n')
c = legalmoves.legal_list(a, 1)
print c


#driverprog.py  legalmoves.py  printboard.py    readchessfileFEN.py  recursemoves.py  treegentest.py
#legalfork.py   poopFEN.py     print_pretty.py  readFENfunc.py       scoreFEN.py

import readFENfunc
import legalmoves
import recursemoves

testpos = readFENfunc.readFEN('rooktest.FEN')
recursemoves.recursemoves(5,testpos,0,0)

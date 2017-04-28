#driverprog.py  legalmoves.py  printboard.py    readchessfileFEN.py  recursemoves.py  treegentest.py
#legalfork.py   poopFEN.py     print_pretty.py  readFENfunc.py       scoreFEN.py

import readFENfunc
import legalmovespawnforkcheck
import recspeedmovescheck
import sys

if len(sys.argv) < 3 or len(sys.argv) > 4:
	print('usage: treegentest FEN_filename searchdepth')
	exit()
for x in sys.argv:
	print x
testpos = readFENfunc.readFEN('FENdir/'+sys.argv[1])
bestline = []
print(str(sys.argv[2]))
a = int(sys.argv[2])
recspeedmovescheck.recursemoves(a,testpos,0,0,bestline,0)
print('bestline is ' + str(bestline))

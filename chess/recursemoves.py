import legalmoves
import scoreFEN
import sys

def recursemoves(depth,FEN_struct,currdepth,whoseturn):#i am reserving the right to adjust depth upwards if the tree is forcing or downwards if it is boring
	if currdepth == depth:
		return 1
	currdepth = currdepth + 1
	movlist = legalmoves.legal_list(FEN_struct,whoseturn)
	for x in movlist:#iirc movlist 
		newfen = FEN_struct
		print('printing newfen:')
		print(newfen)
		newfen[x[0]][x[1]] = '*'
		newfen[x[2]][x[3]] = FEN_struct[x[2]][x[3]]
		if whoseturn == 0:
			whoseturn = 1
		else:
			whoseturn = 0
		recursemoves(depth,newfen,currdepth,whoseturn)

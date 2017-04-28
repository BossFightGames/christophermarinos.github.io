import legalmovespawnforkcheck
import scoreFEN
import printboard
import sys
import copy

def recursemoves(depth,FEN_struct,currdepth,whoseturn,bestline,scorediff):#i am reserving the right to adjust depth upwards if the tree is forcing or downwards if it is boring
	
	if currdepth >= depth:
		return scoreFEN.score_FEN(FEN_struct)
	numrecursions = 0#bump this up every time we recurse; if it remains 0 at exit we have a stale or checkmate situation
	finalscore = -99999
	currdepth = currdepth + 1
	reclist = []
	legalmovlist = []
	legalmovlist = legalmovespawnforkcheck.legal_list(FEN_struct,whoseturn)
	print legalmovlist
	if legalmovlist == 'X':
		return 0
	for x in legalmovlist:
	#leave bestline alone right now
#		currFEN_struct = list(FEN_struct)#important otherwise we have a reference and we dont want that ie newstruct = FEN_struct is wrong wrong wrong :)	
		currFEN_struct = copy.deepcopy(FEN_struct)
		currFEN_struct[x[0]][x[1]] = '*'
		xfo = x[4]
		currFEN_struct[x[2]][x[3]] = xfo
		print('altered FEN_struct added to list: ') 
		printboard.printboard(currFEN_struct)
		reclist.append(currFEN_struct)
	del(FEN_struct)
	if whoseturn == 0:
		currturn = 1
	else:
		currturn = 0
	for x in reclist:
		numrecursions = numrecursions + 1
		sc = scoreFEN.score_FEN(currFEN_struct)
		diffsc = sc - scorediff
		if diffsc == 0:
			currdepth = currdepth +.3
		else:
			currdepth = currdepth -1#at the very least stall until we can work out the forcing moves
		currdepth = currdepth + 1
		testscore = recursemoves(depth,x,currdepth, currturn,bestline,sc)
		if testscore > finalscore:
			finalscore = testscore
	if numrecursions == 0:
		print('CHECK OR STALEMATE FOUND')
	return finalscore	

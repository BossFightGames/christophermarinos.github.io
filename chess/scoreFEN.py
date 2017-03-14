#1-3-3-5-9 for pawn B/N N/B R Q repsectively with the king, obviously, being infinite
#hella easy to start: ability to castle is .25, so we dont lightly sacrifice material to make opp lose it
#perhaps later make central square influence worth .05 or something so we dont open pawn to a4 or Knight to h3
#so take a fen as input, return an integer value
#we are concerned about the difference between the black and white scores. +/- .75 to 1 is a decisive advantage, anything over that is crushing
#chess, although it has a history of dynamic brilliancies, is a highly materialistic game. if you are up material, even a pawn, you are winning IN GENERAL
#because of this it is possible to makr an engine evaluation care only about greed (maybe setting central control to a slight +) and crush everyone with processing power
#last but not least we aren't going to throw a whose side is it conditional into the mix. if score is + white has an advantage if score is - black does
QUEEN      = 9
ROOK       = 5
BISHOP     = 3
KNIGHT     = 3
PAWN       = 1
CAN_CASTLE = .25



def score_FEN(FEN_struct):
	score = 0.0
	for i in range(8):
		for j in range(8):
			if FEN_struct[i][j] =='p':
				score = score - PAWN 
			if FEN_struct[i][j] =='P':
                                score = score + PAWN
                        if FEN_struct[i][j] =='q':
                                score = score - QUEEN
                        if FEN_struct[i][j] =='Q':
                                score = score + QUEEN
                        if FEN_struct[i][j] =='b':
                                score = score - BISHOP
                        if FEN_struct[i][j] =='B':
                                score = score + BISHOP
                        if FEN_struct[i][j] =='n':
                                score = score - KNIGHT
                        if FEN_struct[i][j] =='N':
                                score = score + KNIGHT
	return score

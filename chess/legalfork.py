#given a FEN array, plus an additional hash of can castle, get legal moves
#1. get all legal moves ignoring check
#2. for each legal move, add to final position IFF our king is not in check
#soooo... what is in FEN_struct? perhaps a dictionary that contains the positions of each piece sorted by type for each color?
def append_mov(FEN_struct,currx,curry,movx,movy):#this function was getting cutpasted everywhere i added to mov and it was inexcusable
	mov = []
	mov.append(currx)
	mov.append(curry)
	mov.append(movx)
	mov.append(movy)
	mov.append(FEN_struct[currx][curry])
	return mov	

def pawn_moves(FEN_struct,turn,movx,movy,movlist):#pawns are a special case nightmare. could a piece like this have ever come about in a post-computational world?
	blek = ['p','r','q','n','b','k']
        alb  = ['P','R','Q','N','B','K']
	#if i am on the second row
	if turn == 0:#if it is white's turn
		if FEN_struct[movx-1][movy] == '*':
			print('adding single pawn move')
			#movlist.append(append_mov(FEN_struct,movx,movy,movx-1,movy))
			mov = []
                        mov.append(movx)
                        mov.append(movy)
                        mov.append(movx-1)
                        mov.append(movy)
                        movlist.append(mov)
			if movx == 1:#if we are on the home square we can move one or two squares
				if FEN_struct[movx][movy+2] == '*':#only if we can move one square do we check two squares ahead
					print('adding double square move')
					mov = []
		                        mov.append(movx)
                		        mov.append(movy)
					mov.append(movx)
                        		mov.append(movy+2)
                        		movlist.append(mov)
		if FEN_struct[movx+1][movy+1] in blek and movx != 7:# if we are not a rightmost rook pawn and can take on the right
 			print('adding pawn capture right')
			mov = []
			mov.append(movy)
			mov.append(movx)
			mov.append(movy+1)
			mov.append(movx+1)
			movlist.append(mov)
                if movx != 0:# if we are not a leftmost rook pawn we can take on the left
			if FEN_struct[movx-1][movy+1] in blek:
				print('adding pawn capture left')
                        	mov = []
                        	mov.append(movy)
                        	mov.append(movx)
                        	mov.append(movy+1)
                        	mov.append(movx-1)
                        	movlist.append(mov)
	return movlist


def rook_moves(FEN_struct,turn,movx,movy,movlist):
	#up and down
	blek = ['p','r','q','n','b','k']
	alb  = ['P','R','Q','N','B','K']
	currx = movx
	curry = movy
	while(1):#go down the column; perhaps finesse an iterator, do it in one pass?
		if currx + 1 > 7:#next move is off the side of the board: bail
			break
		if FEN_struct[currx+1][movy] in alb:#this is a capture. we cannot capture past an enemy piece so record the move and bail
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx+1)
			mov.append(curry)
			movlist.append(mov)
			break
		if FEN_struct[currx+1][movy] in blek:#this is a friendly piece. we cannot capture past this so (for god's sake) do not record it as a valid move and bail
			break
		#we have a blank space so record as valid move and then increment currx and repeat
		print('adding moves')
		mov = []
		mov.append(movx)
		mov.append(movy)
		mov.append(currx+1)
		mov.append(curry)
		movlist.append(mov)
		currx = currx + 1
	currx = movx
	curry = movy
	while(1):
		if currx - 1 < 0:
			break
		if FEN_struct[currx-1][movy] in alb:
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx-1)
			mov.append(curry)
			movlist.append(mov)
			break
		if FEN_struct[currx-1][movy] in blek:
			break
		print('adding moves')
		mov = []
		mov.append(movx)
		mov.append(movy)
		mov.append(currx-1)
		mov.append(curry)
		movlist.append(mov)
		currx = currx - 1
	currx = movx
	curry = movy
	while(1):
		if curry + 1 > 7:
			break
		if FEN_struct[currx][movy+1] in alb:
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx)
			mov.append(curry+1)
			movlist.append(mov)
			break
		if FEN_struct[movx][curry+1] in blek:
			break
		print('adding moves')
		mov = []
		mov.append(movx)
		mov.append(movy)
		mov.append(currx)
		mov.append(curry+1)
		curry = curry + 1
	currx = movx
	curry = movy
	while(1):
		if curry - 1 < 0:
			break
		if FEN_struct[currx][curry-1] in alb:
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx)
			mov.append(curry-1)
			break
		if FEN_struct[currx][curry - 1] in blek:
			break
		print('adding moves')
		mov = []
		mov.append(movx)
		mov.append(movy)
		mov.append(currx)
		mov.append(curry-1)
		curry = curry -1
		
	
	return movlist

	
#def king_moves(FEN_struct,turn,movlist):#run this after whatever else we ran unless it was a king move or something#this comment makes no sense
#def queen_moves(FEN_struct,turn,movlist):
#def bishop_moves(FEN_struct,turn,movlist):
#def knight_moves(FEN_struct,turn,movlist):
def legal_list(FEN_struct,turn):#Python loves the colons
	retlist = []#this gets passed around to functions
	print('hello\n') 
	for i in range (8):
		for j in range (8):
		#	print('testing R versus ')
			if FEN_struct[i][j] == 'R':
				print(FEN_struct[i][j])
				print('testing for rook moves\n')
				retlist = rook_moves(FEN_struct,0,i,j,retlist)
			if FEN_struct[i][j] == 'P':
				print(FEN_struct[i][j])
				print('testing for pawn moves\n')
				retlist = pawn_moves(FEN_struct,0,i,j,retlist)
				print retlist
	return retlist
					
			
def are_we_live():
	print('yeahhhhhh!!!!\n')

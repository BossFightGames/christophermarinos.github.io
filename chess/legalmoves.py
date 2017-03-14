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

def bishop_moves(FEN_struct,turn,movx,movy,movlist):
	blek = ['p','r','q','n','b','k']
        alb  = ['P','R','Q','N','B','K']
	enemy  = []
	friend = []
	
	if turn == 0:
		enemy  = blek
		friend = alb
	if turn == 1:
		enemy  = alb
		friend = blek
	# +x +y, -x -y, +x -y, -x +y
	# this is a pain in tarse because i also have to set my board limits relative to whether we are > || < 1 
	# so let's give it a shot
	for x in range(4):#the strategy in here can also be used to handle rook moves by setting either incx or incy to 0
		if x == 0:
			incx = 1
			incy = 1
			offboardx = 8
			offboardy = 8
		if x == 1:
			incx = - 1
			incy = -1
			offboardx = -1
			offboardy = -1
		if x == 2:
			incx = 1
			incy = -1
			offboardx = 8
			offboardy = -1
		if x == 3:
			incx = -1
			incy = 1
			offboardx = -1
			offboardy = 8
		currx = movx
		curry = movy
		#having sidestepped a ton of cut/paste and the attendant nasty errors...
		while 1:#infinite while since we are guaranteed to get out: this bails at the side of the board if we dont hit a capture or friendly piece first
			if (currx + incx) == offboardx or (curry + incy) == offboardy:
				break 
			currx = currx + incx
			curry = curry + incy
			if FEN_struct[currx][curry] in friend:
				break#can't take through a friendly piece; done and of course let's not capture it :)
			if FEN_struct[currx][curry] in enemy:
				movlist.append(append_mov(FEN_struct,movx,movy,currx,curry))
				break#can't take after a capture, done
			#empty square (it isn't friendly, isn't an enemy and isn't off the board) add the move
			movlist.append(append_mov(FEN_struct,movx,movy,currx,curry))
	return movlist	
	
def knight_moves(FEN_struct,turn,movx,movy,movlist):
	blek = ['p','r','q','n','b','k']
        alb  = ['P','R','Q','N','B','K']

        if turn == 0:
                enemy  = blek
                friend = alb
        if turn == 1:
                enemy  = alb
                friend = blek

	#N moves wicked easy: if it is off the board dont bother, if it is blank of enemy write it down, if it is friendly dont move. Knights cannot be blocked!! hooray!!!!
	#to make N moves: add two to one axis then +1 and -1 the other axis, then -2 and same, then switch axes. Can this be extended to multiple dimensions?
	plus2x = movx+2
	min2x  = movx-2
	plus1x = movx+1
	min1x  = movx-1
	plus2y = movy+2
	min2y  = movy-2
	min1y  = movy-1
	plus1y = movy+1

	#check +2 first then check the +/- 1s
	if plus2x <= 7:
		if plus1y <= 7:
			if FEN_struct[plus2x][plus1y] in enemy:
				movlist.append(append_mov(FEN_struct,movx,movy,plus2x,plus1y))
			if FEN_struct[plus2x][plus1y] == '*':#or whatever we end up using for blank
				movlist.append(append_mov(FEN_struct,movx,movy,plus2x,plus1y))
		if min1y >= 0:
			if FEN_struct[plus2x][min1y] in enemy:
                                movlist.append(append_mov(FEN_struct,movx,movy,plus2x,min1y))
                        if FEN_struct[plus2x][min1y] == '*':#or whatever we end up using for blank
				movlist.append(append_mov(FEN_struct,movx,movy,plus2x,mint1y))
	                       
	if min2x  >= 0:
		if plus1y <= 7:
                        if FEN_struct[min2x][plus1y] in enemy:
                                movlist.append(append_mov(FEN_struct,movx,movy,min2x,plus1y))
                        if FEN_struct[min2x][plus1y] == '*':#or whatever we end up using for blank
				movlist.append(append_mov(FEN_struct,movx,movy,min2x,plus1y))
                if min1y  >= 0:
                        if FEN_struct[min2x][min1y] in enemy:
                                movlist.append(append_mov(FEN_struct,movx,movy,min2x,min1y))
                        if FEN_struct[min2x][min1y] == '*':#or whatever we end up using for blank
                                 movlist.append(append_mov(FEN_struct,movx,movy,min2x,min1y))

	if plus2y <= 7:
                if plus1x <= 7:
                        if FEN_struct[plus1x][plus2y] in enemy:
                                movlist.append(append_mov(FEN_struct,movx,movy,plus1x,plus2y))
                        if FEN_struct[plus1x][plus2y] == '*':#or whatever we end up using for blank
                                 movlist.append(append_mov(FEN_struct,movx,movy,plus1x,plus2y))

                if min1x  >= 0:
                        if FEN_struct[min1x][plus2y] in enemy:
                                movlist.append(append_mov(FEN_struct,movx,movy,min1x,plus2y))
                        if FEN_struct[min1x][plus2y] == '*':#or whatever we end up using for blank
                                 movlist.append(append_mov(FEN_struct,movx,movy,min1x,plus2y))
        if min2y  >= 0:
                if plus1x <= 7:
                        if FEN_struct[plus1x][min2y] in enemy:
                                movlist.append(append_mov(FEN_struct,movx,movy,plus1x,min2y))
                        if FEN_struct[plus1x][min2y] == '*':#or whatever we end up using for blank
                                 movlist.append(append_mov(FEN_struct,movx,movy,plus1x,min2y))

                if min1x  >= 0:
                        if FEN_struct[min1x][min2y] in enemy:
                                movlist.append(append_mov(FEN_struct,movx,movy,min1x,min2y))
                        if FEN_struct[min1x][min2y] == '*':#or whatever we end up using for blank
                                 movlist.append(append_mov(FEN_struct,movx,movy,min1x,min2y))
	return movlist


def pawn_moves_white(FEN_struct,turn,movx,movy,movlist):#pawns are a special case nightmare. could a piece like this have ever come about in a post-computational world?
	blek = ['p','r','q','n','b','k']
        alb  = ['P','R','Q','N','B','K']
	#if i am on the second row
	if turn == 0:#if it is white's turn
		if FEN_struct[movx-1][movy] == '*':#as long as we check for promotion first we dont have to bounds check this
			#print('adding single pawn move')
			mov = []
                        mov.append(movx)
                        mov.append(movy)
                        mov.append(movx-1)
                        mov.append(movy)
                        movlist.append(mov)
			if movx == 6:#if we are on the home square we can move one or two squares
				if FEN_struct[movx-2][movy] == '*':#only if we can move one square do we check two squares ahead
					#print('adding double square move')
					mov = []
		                        mov.append(movx)
                		        mov.append(movy)
					mov.append(movx-2)
                        		mov.append(movy)
                        		movlist.append(mov)
		if movx != 7 and movy != 7:
			if FEN_struct[movx+1][movy+1] in blek:# if we are not a rightmost rook pawn and can take on the right
 				print('adding pawn capture right')
				mov = []
				mov.append(movy)
				mov.append(movx)
				mov.append(movy+1)
				mov.append(movx+1)
				movlist.append(mov)
                if movx != 0 and movy !=7:# if we are not a leftmost rook pawn we can take on the left
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

        enemy  = []
        friend = []

        if turn == 0:
                enemy  = blek
                friend = alb
        if turn == 1:
                enemy  = alb
                friend = blek

	currx = movx
	curry = movy
	while(1):#go down the column; perhaps finesse an iterator, do it in one pass?
		if currx + 1 > 7:#next move is off the side of the board: bail
			break
		if FEN_struct[currx+1][movy] in blek:#this is a capture. we cannot capture past an enemy piece so record the move and bail
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx+1)
			mov.append(curry)
			movlist.append(mov)
			break
		if FEN_struct[currx+1][movy] in alb:#this is a friendly piece. we cannot capture past this so (for god's sake) do not record it as a valid move and bail
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
		if FEN_struct[currx-1][movy] in blek:
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx-1)
			mov.append(curry)
			movlist.append(mov)
			break
		if FEN_struct[currx-1][movy] in alb:
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
		if FEN_struct[currx][movy+1] in blek:
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx)
			mov.append(curry+1)
			movlist.append(mov)
			break
		if FEN_struct[movx][curry+1] in alb:
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
		if FEN_struct[currx][curry-1] in blek:
			print('adding moves')
			mov = []
			mov.append(movx)
			mov.append(movy)
			mov.append(currx)
			mov.append(curry-1)
			break
		if FEN_struct[currx][curry - 1] in alb:
			break
		print('adding moves')
		mov = []
		mov.append(movx)
		mov.append(movy)
		mov.append(currx)
		mov.append(curry-1)
		curry = curry -1
		
	
	return movlist

def king_moves(FEN_struct,turn,movx,movy,movlist):#king moves is a mess of ifs and bounds checking i am sure this could have been better handled
        blek = ['p','r','q','n','b','k']
        alb  = ['P','R','Q','N','B','K']
        
	enemy  = []
        friend = []
        if turn == 0:
                enemy  = blek
                friend = alb
        if turn == 1:
                enemy  = alb
                friend = blek
	x = movx
	y = movy
	#test x+1,y x-1,y x,y+1 x,y-1 x+1,y-1 x-1,y+1, x+1,y+1 y-1,x-1
	if (x + 1) < 8:
		if FEN_struct[x+1][y] in enemy or FEN_struct[x+1][y] == '*':
			movlist.append(append_mov(FEN_struct,movx,movy,movx+1,movy))
		if (y+1) < 8:
			if FEN_struct[x+1][y+1] in enemy or FEN_struct[x+1][y+1] == '*':
				movlist.append(append_mov(FEN_struct,movx,movy,movx+1,movy+1))
		if (y-1) > 0:
			if FEN_struct[x+1][y-1] in enemy or FEN_struct[x+1][y-1] == '*':
				movlist.append(append_mov(FEN_struct,movx,movy,movx+1,movy-1))

	if (x - 1) > 0:
		if (y+1) < 8:
			if FEN_struct[x-1][y+1] in enemy or FEN_struct[x-1][y+1] == '*':
				movlist.append(append_mov(FEN_struct,movx,movy,movx-1,movy+1))
		if (y-1) > 0:
			if FEN_struct[x-1][y-1] in enemy or FEN_struct[x-1][y-1] == '*':
				movlist.append(append_mov(FEN_struct,movx,movy,movx-1,movy-1))
		if FEN_struct[x-1][y]   in enemy or FEN_struct[x-1][y]   == '*':
			 movlist.append(append_mov(FEN_struct,movx,movy,movx-1,movy))
	if (y - 1) > 0:
		if FEN_struct[x][y-1] in enemy or FEN_struct[x][y-1] == '*':
			movlist.append(append_mov(FEN_struct,movx,movy,movx,movy-1))
	if (y + 1) < 8:
		if FEN_struct[x][y+1] in enemy or FEN_struct[x][y+1] == '*':
			movlist.append(append_mov(FEN_struct,movx,movy,movx,movy+1))
	#OOPS FORGOT CASTLING
	return movlist


#def am_i_in_check(movx,movy,turn):#king capture makes this easy to implement at the cost of some computational complexity
	#from the king's position do rook, bishop N, pawn AND king tests
	
#def king_moves(FEN_struct,turn,movlist):#run this after whatever else we ran unless it was a king move or something#this comment makes no sense
#def queen_moves(FEN_struct,turn,movlist):
#def bishop_moves(FEN_struct,turn,movlist):
#def knight_moves(FEN_struct,turn,movlist):
def legal_list(FEN_struct,turn):#Python loves the colons
	retlist = []#this gets passed around to functions
	for i in range (8):
		for j in range (8):
		#	print('testing R versus ')
			if FEN_struct[i][j] == 'R':
				#print('testing for rook moves\n')
				retlist = rook_moves(FEN_struct,0,i,j,retlist)
			if FEN_struct[i][j] == 'P':
				#print('testing for pawn moves\n')
				retlist = pawn_moves_white(FEN_struct,0,i,j,retlist)
			if FEN_struct[i][j] == 'N':
				#print('testing for N moves\n')
				retlist = knight_moves(FEN_struct,0,i,j,retlist)
			if FEN_struct[i][j] == 'B':
				#print('testing for B moves\n')
				retlist = bishop_moves(FEN_struct,0,i,j,retlist)
			if FEN_struct[i][j] == 'Q':
				#print('testing for Q moves\n')
				retlist = rook_moves(FEN_struct,0,i,j,retlist)
				retlist = bishop_moves(FEN_struct,0,i,j,retlist)
			if FEN_struct[i][j] == 'K':#the boss
				#print('testing for K moves\n')
				retlist = king_moves(FEN_struct,0,i,j,retlist)
	print retlist
	return retlist
					
			

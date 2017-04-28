#given a FEN array, plus an additional hash of can castle, get legal moves
#1. get all legal moves ignoring check
#2. for each legal move, add to final position IFF our king is not in check
#soooo... what is in FEN_struct? perhaps a dictionary that contains the positions of each piece sorted by type for each color?
#ok we are going to change FEN_struct where is is now a list where FEN_struct[0] has what used to be FEN_struct andf FS[1] is can_castle true/false and last but not least legal pos which is set t/f then the rec func chops down illegal positions
#we can still save time by dumnping out of the func when we can check the king
movesdictalb  = {'king': 'K', 'queen':'Q','bishop':'B','knight':'N','rook':'R','pawn':'P'}
movesdictblek = {'king': 'k', 'queen':'q','bishop':'b','knight':'n','rook':'r','pawn':'p'}
blek = ['p','r','q','n','b','k']
alb  = ['P','R','Q','N','B','K']

king_castle_alb  =[7,4]
king_castle_blek =[0,4]

def append_mov(FEN_struct,currx,curry,movx,movy):#this function was getting cutpasted everywhere i added to mov and it was inexcusable
	mov = []
	mov.append(currx)
	mov.append(curry)
	mov.append(movx)
	mov.append(movy)
	mov.append(FEN_struct[currx][curry])
	return mov
	

def bishop_moves(FEN_struct,turn,movx,movy,movlist):#the right way to do it. current implememtation of rook moves is the wrong way
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
                                if FEN_struct[currx][curry] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,currx,curry))
				break#can't take after a capture, done
			#empty square (it isn't friendly, isn't an enemy and isn't off the board) add the move
			movlist.append(append_mov(FEN_struct,movx,movy,currx,curry))
	return movlist	
	
def knight_moves(FEN_struct,turn,movx,movy,movlist):
	enemy =  []
	friend = []
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
				if FEN_struct[plus2x][plus1y] == enemy[5]:
					return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,plus2x,plus1y))
#				return movlist
			if FEN_struct[plus2x][plus1y] == '*':#or whatever we end up using for blank
				movlist.append(append_mov(FEN_struct,movx,movy,plus2x,plus1y))
#				return movlist
		if min1y >= 0:
			if FEN_struct[plus2x][min1y] in enemy:
                                if FEN_struct[plus2x][min1y] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,plus2x,min1y))
#				return movlist
                        if FEN_struct[plus2x][min1y] == '*':#or whatever we end up using for blank
				movlist.append(append_mov(FEN_struct,movx,movy,plus2x,min1y))
#				return movlist
	                       
	if min2x  >= 0:
		if plus1y <= 7:
                        if FEN_struct[min2x][plus1y] in enemy:
                                if FEN_struct[min2x][plus1y] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,min2x,plus1y))
#				return movlist
                        if FEN_struct[min2x][plus1y] == '*':#or whatever we end up using for blank
				movlist.append(append_mov(FEN_struct,movx,movy,min2x,plus1y))
#				return movlist
                if min1y  >= 0:
                        if FEN_struct[min2x][min1y] in enemy:
                                if FEN_struct[min2x][min1y] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,min2x,min1y))
#				return movlist
                        if FEN_struct[min2x][min1y] == '*':#or whatever we end up using for blank
                                movlist.append(append_mov(FEN_struct,movx,movy,min2x,min1y))
#				return movlist

	if plus2y <= 7:
                if plus1x <= 7:
                        if FEN_struct[plus1x][plus2y] in enemy:
                                if FEN_struct[plus1x][plus2y] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,plus1x,plus2y))
#				return movlist
                        if FEN_struct[plus1x][plus2y] == '*':#or whatever we end up using for blank
                                movlist.append(append_mov(FEN_struct,movx,movy,plus1x,plus2y))
#				return movlist

                if min1x  >= 0:
                        if FEN_struct[min1x][plus2y] in enemy:
                                if FEN_struct[min1x][plus2y] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,min1x,plus2y))
#				return movlist
                        if FEN_struct[min1x][plus2y] == '*':#or whatever we end up using for blank
                                movlist.append(append_mov(FEN_struct,movx,movy,min1x,plus2y))
#				return movlist
        if min2y  >= 0:
                if plus1x <= 7:
                        if FEN_struct[plus1x][min2y] in enemy:
                                if FEN_struct[plus1x][min2y] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,plus1x,min2y))
#				return movlist
                        if FEN_struct[plus1x][min2y] == '*':#or whatever we end up using for blank
                                movlist.append(append_mov(FEN_struct,movx,movy,plus1x,min2y))
#				return movlist

                if min1x  >= 0:
                        if FEN_struct[min1x][min2y] in enemy:
                                if FEN_struct[min1x][min2y] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,min1x,min2y))
#				return movlist
                        if FEN_struct[min1x][min2y] == '*':#or whatever we end up using for blank
                                movlist.append(append_mov(FEN_struct,movx,movy,min1x,min2y))
#				return movlist
	return movlist

#def append_mov(FEN_struct,currx,curry,movx,movy)://for reference
def pawn_moves(FEN_struct,turn,movx,movy,movlist):#pawns are a special case nightmare. could a piece like this have ever come about in a post-computational world?
	white_homex = 6#magic numbers designating the home squares due to me screwing up my notation (and fixing w a software layer) 
	black_homex = 1
	white_promotex = 0
	black_promotex = 7
	#if i am on the second row
	if turn == 0:#if it is white's turn
		enemy = blek
		friend = alb#duh pawns don't care about friends just enemies and blank squares to move onto
		xadv = -1
		ycapr = 1
		ycapl = -1
		homex = white_homex
		offboardleft  = -1 
		offboardright = 8
		offboardvert  = -1
		promotex = white_promotex
	else:
		enemy = alb
		friend = blek
		xadv = 1
		ycapr = 1
		ycapl = -1
		homex = black_homex
		offboardleft  = 8
		offboardright = -1
		offboardvert = 8
		promotex = black_promotex
	
	if movx == promotex:
			print('PROMOTING')
			move = []
			move.append(movx)
			move.append(movy)
			move.append(movx)
			move.append(movy)
			move.append(friend[2])
			movlist.append(move)
			return movlist
	if FEN_struct[movx+xadv][movy] == '*':#as long as we check for promotion first we dont have to bounds check this
		movlist.append(append_mov(FEN_struct,movx,movy,movx+xadv,movy))
		#mov = []
                #mov.append(movx)
                #mov.append(movy)
                #mov.append(movx-1)
                #mov.append(movy)
                #movlist.append(mov)
		if movx == 6:#if we are on the home square we can move one or two squares
			if (movx + (xadv * 2)) != -1 and (movx + (xadv * 2)) != 8:
				if FEN_struct[movx + (xadv * 2)][movy] == '*':#only if we can move one square do we check two squares aheadi
					print('FEN STRUCT ' )
					print(FEN_struct[movx + (xadv * 2)][movy])
					print('EQUALS *')
					movlist.append(append_mov(FEN_struct,movx,movy,movx+ (2*xadv),movy))#one of 'em moves one square, two of 'em move two
		if (movx+xadv) != 8 and (movx+xadv) != -1 and (movy+ycapr) != 8 and (movy+ycapr) != -1:
			if FEN_struct[movx + xadv][movy+ ycapr] in enemy:# if we are not a rightmost rook pawn and can take on the right
                                if FEN_struct[movx + xadv][movy + ycapr] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,movx+xadv,movy+ycapr))
                if (movx+xadv) != 8 and (movx+xadv) != -1  and (movy + ycapl) != -1 and (movy + ycapl) != 8 :# if we are not a leftmost rook pawn we can take on the left
			if FEN_struct[movx + xadv][movy+ycapl] in enemy:
                                if FEN_struct[movx+xadv][movy+ycapl] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,movx,movy))
	return movlist


def rook_moves(FEN_struct,turn,movx,movy,movlist):
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
                        incy = 0
                        offboardx = 8
                        offboardy = 8
                if x == 1:
                        incx = - 1
                        incy = 0
                        offboardx = -1
                        offboardy = -1
                if x == 2:
                        incx = 0
                        incy = -1
                        offboardx = 8
                        offboardy = -1
                if x == 3:
                        incx = 0
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
                                if FEN_struct[currx][curry] == enemy[5]:
                                        return 'X'#return nil???????
                                movlist.append(append_mov(FEN_struct,movx,movy,currx,curry))
                                break#can't take after a capture, done
                        #empty square (it isn't friendly, isn't an enemy and isn't off the board) add the move
                        movlist.append(append_mov(FEN_struct,movx,movy,currx,curry))

	return movlist

def king_moves(FEN_struct,turn,movx,movy,movlist):#king moves is a mess of ifs and bounds checking i am sure this could have been better handled
	enemy  = []
        friend = []
        if turn == 0:
                enemy  = blek
                friend = alb
		castle_pos = king_castle_alb
        if turn == 1:
                enemy  = alb
                friend = blek
		castle_pos = king_castle_blek
	x = movx
	y = movy

	#test x+1,y x-1,y x,y+1 x,y-1 x+1,y-1 x-1,y+1, x+1,y+1 y-1,x-1
	#new method: push all king moves onto a list and eliminate the out of bounds ones
	#other idea: make a check board where all pieces write their potential moves onto a board and then the king cant go there???
	if (x + 1) < 8:
		if FEN_struct[x+1][y] in enemy or FEN_struct[x+1][y] == '*':
			movlist.append(append_mov(FEN_struct,movx,movy,movx+1,movy))
		if (y+1) < 8:
			if FEN_struct[x+1][y+1] in enemy or FEN_struct[x+1][y+1] == '*':
                                if FEN_struct[x+1][y+1] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,movx+1,movy+1))
		if (y-1) > 0:
			if FEN_struct[x+1][y-1] in enemy or FEN_struct[x+1][y-1] == '*':
                                if FEN_struct[x+1][y-1] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,movx+1,movy-1))

	if (x - 1) > 0:
		if (y+1) < 8:
			if FEN_struct[x-1][y+1] in enemy or FEN_struct[x-1][y+1] == '*':
                                if FEN_struct[x-1][y+1] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,movx-1,movy+1))
		if (y-1) > 0:
			if FEN_struct[x-1][y-1] in enemy or FEN_struct[x-1][y-1] == '*':
                                if FEN_struct[x-1][y-1] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,movx-1,movy-1))
		if FEN_struct[x-1][y]   in enemy or FEN_struct[x-1][y]   == '*':
                                if FEN_struct[x-1][y] == enemy[5]:
                                        return 'X'#return nil???????
			 	movlist.append(append_mov(FEN_struct,movx,movy,movx-1,movy))
	if (y - 1) > 0:
		if FEN_struct[x][y-1] in enemy or FEN_struct[x][y-1] == '*':
                                if FEN_struct[x][y-1] == enemy[5]:
                                        return 'X'#return nil???????
				movlist.append(append_mov(FEN_struct,movx,movy,movx,movy-1))
	if (y + 1) < 8:
		if FEN_struct[x][y+1] in enemy or FEN_struct[x][y+1] == '*':
                                if FEN_struct[x][y+1] == enemy[5]:
                                        return 'X'#return nil???????
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
	if turn == 0:
		mydict = movesdictalb
	if turn == 1:
		mydict = movesdictblek
	for i in range (8):
		for j in range (8):
			if FEN_struct[i][j] == mydict["rook"]:
				retlist = rook_moves(FEN_struct,turn,i,j,retlist)
			if retlist == 'X':
				return retlist
			if FEN_struct[i][j] == mydict["pawn"]:
				retlist = pawn_moves(FEN_struct,turn,i,j,retlist)
                        if retlist == 'X':
                                return retlist
			if FEN_struct[i][j] == mydict["knight"]:
				retlist = knight_moves(FEN_struct,turn,i,j,retlist)
                        if retlist == 'X':
                                return retlist
			if FEN_struct[i][j] == mydict["bishop"]:
				retlist = bishop_moves(FEN_struct,turn,i,j,retlist)
                        if retlist == 'X':
                                return retlist
			if FEN_struct[i][j] == mydict["queen"]:
				retlist = rook_moves(FEN_struct,turn,i,j,retlist)
                        if retlist == 'X':
                                return retlist
				retlist = bishop_moves(FEN_struct,turn,i,j,retlist)
                        if retlist == 'X':
                                return retlist
			if FEN_struct[i][j] == mydict["king"]:#the boss
				retlist = king_moves(FEN_struct,turn,i,j,retlist)
                        if retlist == 'X':#EEEEEP the kings are touching!!!
                                return retlist
	return retlist
					
			

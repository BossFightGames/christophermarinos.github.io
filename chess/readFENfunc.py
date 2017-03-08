def readFEN(FENname):
	fpr = open(FENname,'r')#file pointer read
	row = fpr.read().split('/')
	gamedata = row[7]#since this is a chess engine and once the rows become > or < 7 it ceases to be chess c programmer's disease/ magic nmbers are acceptable but I still keep an eye on them
	chessboard = []
	row[7] = row[7].split(' ')[0]#strip off the castling, whose move is it, total # moves etc stuff sow row[0-7] are just the rows of the chessboard
	print row
	print 'printed row now proceeding to test isdigit function'
	for x in row:
		addrow = [];
		for i in x:
			if i.isdigit():
				a = int(i)
				for j in range(0,a):
					addrow.append('*')#ffs do not append 'b' for blank because ti collides with 'b' for black bishop
			else:
				addrow.append(i)
		chessboard.append(addrow)
	return chessboard

import sys#once again for a command line arg
#this will, given a valid FEN file, print out an ASCII boardi
def printboard(board):
	a = []
	print ('________________')
	for x in board:#rows
		print('|' + x[0] + '|' +  x[1] + '|' +  x[2] +'|' +  x[3] + '|' +  x[4] +'|' +  x[5] + '|' +  x[6] + '|' +  x[7]+ '|')
	print ('~~~~~~~~~~~~~~~~')


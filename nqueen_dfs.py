board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = 4

def safe (row,col) :

	for i in range(0,col) :
		if(board[row][i]) :
			return False

	for i,j in zip(range(row,-1,-1),range(col,-1,-1)) :
			if(board[i][j]) :
				return False


	for i,j in zip(range(row,n,1),range(col,-1,-1)) :
			if(board[i][j]) :
				return False

	return True



def sol (col) :
	if (col >= n) :
		return True
	for i in range(0,n) :

		if (safe(i,col)) :

			board[i][col] = 1

			if(sol(col+1)) :
				return True

			board[i][col] = 0

	return False 


def printk():
	for i in range(0,n) :
		for j in range (0,n):
			print(board[i][j] ,end = " ")

		print()		

if(not sol(0)) :
	print("soln doesn't exist")
else :
	printk()




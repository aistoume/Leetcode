### Youbin 2017/07/13
### 529 Minesweeper

class Solution(object):
	def updateBoard(self, board, click):
		(x,y) = click
		neigh = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1))
		if 0<=x<len(board) and 0<=y<len(board[0]):
			if board[x][y]=='M':
				board[x][y]='X'
			elif board[x][y]=='E':
				n = sum([board[x+r][y+c]=='M' for r,c in neigh if 0<=x+r<len(board) and 0<=y+c<len(board[0])])
				board[x][y] = str(n or 'B')
				for i,j in neigh*(not n):
					self.updateBoard(board,[x+i, y+j])
		return board
		
		
		
		
s = Solution()
board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

c = [3, 0]
r = s.updateBoard(board,c)
print r
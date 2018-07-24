# 840. Magic Squares In Grid

class Solution(object):
	def numMagicSquaresInside(self, grid):
		if len(grid)<3 or len(grid[0])<3: return 0
		count = 0
		for i in range(len(grid)-2):
			for j in range(len(grid[0])-2):
				g = [row[j:j+3] for row in grid[i:i+3]]
				if self.isMagic(g):count+=1
		return count 
	def isMagic(self, grid):
		m1 = [[4,3,8],[9,5,1],[2,7,6]]
		m2 = m1[::-1]
		m3 = [i[::-1] for i in m1]
		m4 = m3[::-1]
		m5 = [[4,9,2],[3,5,7],[8,1,6]]
		m6 = m5[::-1]
		m7 = [i[::-1] for i in m5]
		m8 = m7[::-1]
		M = [m1,m2,m3,m4,m5,m6,m7,m8]
		return (grid in M)
		
So = Solution()
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
#grid = [[4,3,8],[9,5,1],[2,7,6]]
g = [i[0:3] for i in grid[0:3]]
print So.numMagicSquaresInside(grid)
#print So.isMagic(grid)
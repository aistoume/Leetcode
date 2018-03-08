### Youbin 2017/06/21
### 463 Island Perimeter

class Solution(object):
    def islandPerimeter(self, grid):
		p = 0
		newGrid = [[0]*(len(grid[0])+2)]
		for l in grid:
			row = [0]+ l + [0]
			newGrid.append(row)
		newGrid.append([0]*(len(grid[0])+2))
		for row in range(1,len(newGrid)-1):
			for col in range(1, len(newGrid[1])-1):
				if newGrid[row][col] == 1:
					if newGrid[row-1][col] == 0:
						p+=1
					if newGrid[row+1][col] == 0:
						p+=1
					if newGrid[row][col-1] == 0:
						p+=1
					if newGrid[row][col+1] == 0:
						p+=1
		return p
	
	
	
s = Solution()
l = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

r = s.islandPerimeter(l)
print r 
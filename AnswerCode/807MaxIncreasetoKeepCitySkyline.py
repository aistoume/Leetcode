# 807. Max Increase to Keep City Skyline

class Solution(object):
	def maxIncreaseKeepingSkyline(self, grid):
		if not grid: return 0
		r,c = len(grid),len(grid[0])
		L2R = [max(sky) for sky in grid]
		T2B = [max([sky[i] for sky in grid]) for i in range(c)]
		ans = 0
		for i in range(r):
			for j in range(c):
				ans+=min(L2R[i], T2B[j])-grid[i][j]
		return ans
	
So = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print So.maxIncreaseKeepingSkyline(grid)
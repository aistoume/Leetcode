# 598 Range Addition II
# Youbin Mo

class Solution(object):
	def maxCount(self, m, n, ops):
		maxX,maxY = m,n
		while ops:
			x,y = ops.pop()
			if x<maxX:
				maxX = x
			if y<maxY:
				maxY =y
		return maxX*maxY
	
	
	
s = Solution()
m,n = 4,5
ops = [[2,3][1,3]]
r = s.maxCount(m,n,ops)
print r

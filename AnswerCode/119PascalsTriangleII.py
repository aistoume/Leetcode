# 119. Pascal's Triangle II

class Solution(object):
	def getRow(self, rowIndex):
		if rowIndex ==0: return [1]
		if rowIndex ==1: return [1,1]
		rowPrev = self.getRow(rowIndex-1)
		return [1]+[(rowPrev[i]+rowPrev[i+1]) for i in range(len(rowPrev)-1)]+[1]
		
So = Solution()
rowIndex = 5
print So.getRow(rowIndex)
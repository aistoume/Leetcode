# 852. Peak Index in a Mountain Array
# Youbin Mo

class Solution(object):
	def peakIndexInMountainArray(self, A):
		for i in range(len(A)-1):
			if A[i]>A[i+1]:
				return i
		return 0
	
	
S = Solution()
A = [0, 1,1,2,3,2, 1, 0]
print S.peakIndexInMountainArray(A)

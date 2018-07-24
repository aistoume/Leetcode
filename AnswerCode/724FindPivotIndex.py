# 724. Find Pivot Index

class Solution(object):
	def pivotIndex(self, nums):
		i = 0
		L,R = 0,sum(nums)
		while i<len(nums):
			if L == R-nums[i]: return i
			L+=nums[i]
			R-=nums[i]
			i+=1
		return -1
		
So = Solution()
nums = [1, 2,3]
print So.pivotIndex(nums)

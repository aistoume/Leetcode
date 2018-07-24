# 645. Set Mismatch

class Solution(object):
	def findErrorNums(self, nums):
		n = len(nums)
		x = (set(range(1,n+1))-set(nums)).pop()
		y = sum(nums)-n*(n+1)/2+x
		return [y,x]
		
So = Solution()
nums = [1,1]
print So.findErrorNums(nums)
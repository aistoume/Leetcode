# 53. Maximum Subarray

class Solution(object):
	def maxSubArray(self, nums):
		m = nums[0]
		L = [nums[0]]
		for i in nums[1:]:
			if i+L[-1]>i: L.append(i+L[-1])
			else: L.append(i)
			m = max(m, L[-1])
		return m
		
So = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print So.maxSubArray(nums)
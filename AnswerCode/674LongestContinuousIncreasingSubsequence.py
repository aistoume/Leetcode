# 674. Longest Continuous Increasing Subsequence

class Solution(object):
	def findLengthOfLCIS(self, nums):
		if len(nums)<2:
			return len(nums)
		ans = 0
		start = 0
		for i in range(1,len(nums)):
			if nums[i]<=nums[i-1]:
				ans = max(ans, i-start)
				start = i
		return max(ans, i-start+1)
	
So = Solution()
input = [1,3,5,7]

print So.findLengthOfLCIS(input)


# 532. K-diff Pairs in an Array

class Solution(object):
	def findPairs(self, nums, k):
		if k<0: return 0
		nums.sort()
		ans = set()
		for i in range(len(nums)):
			a = nums[i]
			if a+k in nums[i+1:]: ans.add((a,a+k))
		return len(ans)
So = Solution()
nums = [3, 2, 4, 1, 5]
k = 1

print So.findPairs(nums,k)
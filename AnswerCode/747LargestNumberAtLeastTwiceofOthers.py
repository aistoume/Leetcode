# 747. Largest Number At Least Twice of Others

class Solution(object):
	def dominantIndex(self, nums):
		if len(nums)<2: return 0
		m = max(nums)
		idx = nums.index(m)
		del nums[idx]
		if max(nums)*2<=m: return idx
		else: return -1
	
	
So = Solution()
nums = [3, 6, 1, 0]
nums = [1, 2, 3, 4]
print So.dominantIndex(nums)

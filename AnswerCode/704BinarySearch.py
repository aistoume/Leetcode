# 704. Binary Search

class Solution(object):
	def search(self, nums, target):
		if target in nums: return nums.index(target)
		else: return -1
So = Solution()
nums = [-1,0,3,5,9,12]
target = 2
print So.search(nums,target)
print nums.index(target)
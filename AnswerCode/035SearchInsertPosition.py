# 35. Search Insert Position

class Solution(object):
	def searchInsert(self, nums, target):
		if target<=nums[0]: return 0
		return [i for i in range(len(nums)) if nums[i]<target][-1]+1

			
So = Solution()
nums = [1,3,5,6]
# nums = [1]
target = 1
print So.searchInsert(nums,target)
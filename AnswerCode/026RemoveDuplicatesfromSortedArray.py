# 26. Remove Duplicates from Sorted Array

class Solution(object):
	def removeDuplicates(self, nums):
		i = 1
		while i <len(nums):
			if nums[i]==nums[i-1]:
				del nums[i]
			else: i+=1
		return len(nums)
		
So = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print So.removeDuplicates(nums)

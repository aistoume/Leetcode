# 217. Contains Duplicate

class Solution(object):
	def containsDuplicate(self, nums):
		dup = set(nums)
		print len(dup)
		if len(dup)==len(nums):
			return False
		return True
nums = [1,2,3,1]
So = Solution()
print So.containsDuplicate(nums)